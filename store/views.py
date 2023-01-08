from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'home.html')


def product(request):
    products = Product.objects.all()
    data = {
        'products': products,
    }
    return render(request, 'product.html', data)


def productDetail(request, pid):
    product = Product.objects.get(id=pid)
    data = {'product': product}
    return render(request, 'product-detail.html', data)


def cart(request):
    return render(request, 'cart.html')


def blog(request):
    return render(request, 'blog.html')


def blogDetail(request):
    return render(request, 'blog-detail.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
