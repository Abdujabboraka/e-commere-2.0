from django.shortcuts import render
from .models import Product, Category, Image
# Create your views here.

def homepage(request):
    categories = Category.objects.exclude(photo='')

    products = Product.objects.all()
    context = {
        'products' : products,
        'categories': categories

    }
    return render(request, 'index.html', context)

def detail(request):

    return render(request, 'ShopApp/detail.html')