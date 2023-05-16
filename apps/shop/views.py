
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Category, Product


class IndexView(View):
    def get(self, request):
        context = {'title': 'E Shop'}
        return render(request, 'shop/index.html', context)


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


class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        context = {
            'title': f'{product.name} - E Shop',
            'product': product,
        }
        return render(request, 'shop/product_detail.html', context)
#
#
# def cart_item_add(request, product_id):
#     product = Product.objects.get(id=product_id)
#     carts = CartItem.objects.filter(user=request.user, product=product)
#
#     if not carts.exists():
#         CartItem.objects.create(user=request.user, product=product, quantity=1)
#     else:
#
#         cart = carts.first()
#         cart.quantity += 1
#         cart.save()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
#
# def cart_item_remove(request, cart_id):
#     cart = CartItem.objects.get(id=cart_id)
#     cart.delete()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])



