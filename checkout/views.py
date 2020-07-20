from django.shortcuts import render, reverse, redirect

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('view_bag'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_AFArHQ41f87rpPWz4EqfOjyk00juU9ZzqD',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)