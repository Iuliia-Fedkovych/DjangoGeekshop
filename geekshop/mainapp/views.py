import json
import random
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from basketapp.models import Basket
from .models import ProductCategory, Product

# Create your views here.


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.filter(is_active=True,
                                      category__is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category,
                                           is_active=True,
                                           category__is_active=True).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    products = Product.objects.filter(is_active=True,
                                      category__is_active=True)[:6]
    basket = get_basket(request.user)

    context = {
        'page_title': 'interior: home page',
        'products': products,
        'basket': basket,
    }
    return render(request, 'mainapp/index.html', context)


def product(request, pk=None, page = 1):
    print(pk)
    categories = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(is_active=True,
                                              category__is_active=True).order_by('price')
            category = {
                'pk':0,
                'name': 'all'
            }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk,
                                              is_active=True,
                                              category__is_active=True).order_by('price')
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(2)
        context = {
            'page_title': 'interior: products',
            'products': products_paginator,
            'categories': categories,
            'category': category,
            'basket': basket,
        }

        return render(request, 'mainapp/interior-product.html', context)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'page_title': 'products',
        'categories': categories,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    return render(request, 'mainapp/interior-product-hot.html', context)


def contact(request):

    basket = get_basket(request.user)

    with open('geekshop/locations.json', 'r', encoding='utf-8') as f:
        locations = json.load(f)

    context = {
        'page_title': 'interior: contacts',
        'locations': locations,
        'basket': basket,
    }
    return render(request, 'mainapp/interior-contact.html', context)


def productdet(request, pk):
    basket = get_basket(request.user)
    categories = ProductCategory.objects.filter(is_active=True)
    product = get_object_or_404(Product, pk=pk)

    context = {
        'page_title': 'interior: product',
        'categories': categories,
        'product': product,
        'basket': basket,
    }
    return render(request, 'mainapp/interior-product-details.html', context)
