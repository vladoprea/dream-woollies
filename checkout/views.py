from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    """
    Determines in the webhook if the user has the save-info box checked.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now,\
                    please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Returns view_bag if bag is empty. Returns checkout template and order form.
    Creates stripe payment intent. Create order in admin checkout.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'county': request.POST['county'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'street_address': request.POST['street_address'],
            'address_addition': request.POST['address_addition'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order = order,
                        product = product,
                        quantity = quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag does not exist in our database."
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There is an error in your form.\
                Please check your informations.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            return redirect(reverse('view_bag'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Prefill the form with the saved info of the user
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.phone_number,
                    'country': profile.country,
                    'postcode': profile.postcode,
                    'town_or_city': profile.town_or_city,
                    'street_address': profile.street_address,
                    'address_addition': profile.address_addition,
                    'county': profile.county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.\
        Did you forget to set it in you environment? ')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts. Checks if the user wants 
    to save their delivery information.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        #Attach the user's profile to the order
        order.user_profile = profile
        order.save()

    # Save the user's info
    if save_info:
        profile_data = {
            'phone_number': order.phone_number,
            'country': order.country,
            'postcode': order.postcode,
            'town_or_city': order.town_or_city,
            'street_address': order.street_address,
            'adress_addition': order.adress_addition,
            'county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    if 'bag' in request.session:
        del request.session['bag']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)