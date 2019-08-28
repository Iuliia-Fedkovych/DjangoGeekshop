import json
from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    context = {
        'page_title': 'interior: home page',
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    all_products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'page_title': 'interior: products',
        'all_products': all_products,
        'categories': categories,
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
    context = {
        'page_title': 'interior: fishnet chair',
    }
    return render(request, 'mainapp/interior-product-details.html', context)
