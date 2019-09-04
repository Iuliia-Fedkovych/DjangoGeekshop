import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    context = {
        'page_title': 'interior: home page',
    }
    return render(request, 'mainapp/index.html', context)


def product(request, pk=None):
    print(pk)
    categories = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all()
            category = {'name': 'all'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk)
        context = {
            'page_title': 'interior: products',
            'products': products,
            'categories': categories,
            'category': category,
        }

        return render(request, 'mainapp/interior-product.html', context)

    products = Product.objects.all()
    context = {
        'page_title': 'interior: products',
        'products': products,
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
    categories = ProductCategory.objects.all()
    context = {
        'page_title': 'interior: fishnet chair',
        'categories': categories
    }
    return render(request, 'mainapp/interior-product-details.html', context)
