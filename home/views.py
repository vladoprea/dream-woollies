from django.shortcuts import render
from products.models import Product

def index(request):
    """ View to return index page """
    products = Product.objects.all()
    products_on_sale = products.filter(on_sale=True)[:4]

    template = 'home/index.html'

    context = {
        'products_on_sale': products_on_sale,
    }
    return render(request, template, context)

def about_us(request):
    """ View that returns the about us page"""
    template = 'home/about_us.html'

    return render(request, template)
