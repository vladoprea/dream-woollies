from django.shortcuts import render
from products.models import Product

def index(request):
    """ View to return index page """
    products = Product.objects.all()
    products_on_sale = products.filter(on_sale=True)

    template = 'home/index.html'

    context = {
        'products_on_sale': products_on_sale,
    }
    return render(request, template, context)
