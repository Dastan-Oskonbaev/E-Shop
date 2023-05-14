from django.db.models import Q
from django.http import request, JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Category, Product, Cart


class IndexView(View):
    def get(self, request):
        context = {'title': 'E Shop'}
        return render(request, 'shop/index.html', context)
# def index(request):
#     context = {'title': 'E Shop'}
#     return render(request, 'shop/index.html', context)


class ShopView(View):
    def get(self, request, category_id=None):
        categories = Category.objects.all()
        products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
        context = {
            'title': 'E Shop - Каталог',
            'categories': categories,
            'products': products,
        }
        return render(request, 'shop/shop.html', context)
# def shop(request, category_id=None):
#     context = {
#         'title': 'E Shop - Каталог',
#         'categories': Category.objects.all(),
#         'products': Product.objects.filter(category_id=category_id) if category_id else Product.objects.all(),
#     }
#     return render(request, 'shop/shop.html', context)

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        context = {
            'title': f'{product.name} - E Shop',
            'product': product,
        }
        return render(request, 'shop/product_detail.html', context)
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

