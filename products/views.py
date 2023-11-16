from django.shortcuts import render
from .models import Product

def product(request):
    
    return render(request, 'products/product.html')

def products(request):
    pro = Product.objects.all()
    # x = {'pro': pro.filter(name = 'ahmed')}
    # x = {'pro': pro.order_by("name")}
    # x = {'pro': pro.exclude(name = 'ahmed')}
    # x = {'pro': pro.count()}
    # x = {'pro': pro.filter(price__exact = 100)}
    # x = {'pro': pro.filter(price__contains = 1)}
    # x = {'pro': pro.filter(price__in = [10, 100])}
    x = {'pro': pro.filter(price__range = [10, 100])}
    return render(request, 'products/products.html', x)