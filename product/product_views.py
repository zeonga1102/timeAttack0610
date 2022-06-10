from django.shortcuts import render, redirect
from .models import Category, Product


# Create your views here.
def home_view(request):
    return redirect('category', 'laptop')


def category_view(request, name):
    categories = Category.objects.all()
    category = Category.objects.get(name=name)
    products = Product.objects.filter(category=category)

    return render(request, 'home.html', {'categories': categories, 'products': products})


def order_view(request, product):
    product_info = Product.objects.get(product=product)
    return render(request, 'order.html', {'product_info': product_info})
