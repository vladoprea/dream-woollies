import math

from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Collection, Review
from .forms import ReviewForm

def all_products(request):
    """ A view to show all products, including sorting and search queries.
        Pagination included for more than 12 products on page
    """

    products_list = Product.objects.all().order_by('id')
    query = None
    collections = None
    collection_page = None
    sort = None
    direction = None
    query_page = None
        
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products_list = products_list.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products_list = products_list.order_by(sortkey)

        if 'collection' in request.GET:
            collections = request.GET['collection'].split(',')
            products_list = products_list.filter(collection__name__in=collections)
            collections = Collection.objects.filter(name__in=collections)
            collection_page = request.GET['collection']

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!\
                                        You were automatically redirected to All Products page.")
                return redirect(reverse('products'))
            query_page = request.GET['q']
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products_list = products_list.filter(queries)

        if 'on_sale' in request.GET:
            products_list = products_list.filter(on_sale=True)
        
    current_sorting = f'{sort}_{direction}'
    total = len(products_list)
    paginator = Paginator(products_list, 12)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {
        'products': products,
        'current_collections': collections,
        'collection_page': collection_page,
        'search_term': query,
        'query_page': query_page,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
        'total': total,
        }


    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show one product's details """
   
    product = get_object_or_404(Product, pk=product_id)
    review_form = ReviewForm()
    reviews = Review.objects.filter(product_id=product_id).order_by('-created_at')
    average_rating = Review.objects.aggregate(Avg('rate')).get('rate__avg') or 1

    context = {
        'product': product,
        'review_form': review_form,
        'reviews': reviews,
        'on_profile_page': True,
        'average_rating': average_rating,
    }

    return render(request, 'products/product_detail.html', context)

def add_review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST': 
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Your review has ben sent. Thank you for your interest.")
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            print('fail')
            print(review_form.errors)
    return redirect(reverse('product_detail', product_id))
        
    