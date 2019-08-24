from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def product(request):
    return render(request, 'mainapp/interior-product.html')


def contact(request):
    return render(request, 'mainapp/interior-contact.html')


def productdet(request):
    return render(request, 'mainapp/interior-product-details.html')
