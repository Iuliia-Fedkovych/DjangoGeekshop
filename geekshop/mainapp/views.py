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
    # locations = [
    #     {
    #         'state': 'California',
    #         'phone': '1900-1234-5678',
    #         'email': 'info-ca@interior.com',
    #         'address': '12 W 1st St, 90001 Los Angeles, California'
    #     },
    #     {
    #         'state': 'Florida',
    #         'phone': '5600-1234-5638',
    #         'email': 'info-fl@interior.com',
    #         'address': '38 W 3st St, 90528 Miami , Florida'
    #     },
    #     {
    #         'state': 'Washington',
    #         'phone': '1200-1484-5695',
    #         'email': 'info-wa@interior.com',
    #         'address': '46 W 5st St, 90853 Seattle, Washington'
    #     },
    # ]

    # with open('geekshop/locations.json', 'w', encoding='utf-8') as f:
    #     json.dump(locations, f)

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
