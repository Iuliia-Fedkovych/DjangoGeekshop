import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    products = Product.objects.all()[:6]
    context = {
        'page_title': 'interior: home page',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context)


def product(request, pk=None):
    print(pk)
    categories = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'page_title': 'interior: products',
            'products': products,
            'categories': categories,
            'category': category,
            'basket': basket,
        }

        return render(request, 'mainapp/interior-product.html', context)

    products = Product.objects.all().order_by('price')
    context = {
        'page_title': 'interior: products',
        'products': products,
        'categories': categories,
        'basket': basket,
    }
    return render(request, 'mainapp/interior-product.html', context)


def contact(request):

    with open('geekshop/locations.json', 'r', encoding='utf-8') as f:
        locations = json.load(f)

    context = {
        'page_title': 'interior: contacts',
        'locations': locations,
    }
    return render(request, 'mainapp/interior-contact.html', context)


def productdet(request):
    categories = ProductCategory.objects.all()
    context = {
        'page_title': 'interior: fishnet chair',
        'categories': categories
    }
    return render(request, 'mainapp/interior-product-details.html', context)
