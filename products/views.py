from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def all_products(request):
    """ A view to show all products, including sorting and search queries.
        Pagination included for more than 12 products on page
    """
    
    products_list = Product.objects.all()
    paginator = Paginator(products_list, 12)

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show one product's details """
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

    