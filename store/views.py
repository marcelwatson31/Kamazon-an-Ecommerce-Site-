from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    context = {}
    return render(request, 'store/main.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

