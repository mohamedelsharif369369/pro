from django.shortcuts import render,redirect,get_object_or_404
from .models import Product


# Create your views here.

    

def products(request):
    product = Product.objects.all()
    return render(request,'products/products.html',{
        'product':product
        })
    return render(request,'',{})
