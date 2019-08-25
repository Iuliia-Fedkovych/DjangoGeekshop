from django.shortcuts import render

# Create your views here.


def main(request):
    context = {
        'page_title': 'interior: home page',
    }
    return render(request, 'mainapp/index.html', context)


def product(request):
    context = {
        'page_title': 'interior: products',
    }
    return render(request, 'mainapp/interior-product.html', context)


def contact(request):
    context = {
        'page_title': 'interior: contacts',
    }
    return render(request, 'mainapp/interior-contact.html', context)


def productdet(request):
    context = {
        'page_title': 'interior: fishnet chair',
    }
    return render(request, 'mainapp/interior-product-details.html', context)
