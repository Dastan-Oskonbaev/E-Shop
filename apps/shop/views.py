from django.db.models import Q
from django.http import request, JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm, RatingForm
from .models import Category, Rating, Product, Cart


def index(request):
    context = {'title': 'E Shop'}
    return render(request, 'shop/index.html', context)


def shop(request, category_id=None):
    context = {
        'title': 'E Shop - Каталог',
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
    }
    return render(request, 'shop/shop.html', context)



def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

