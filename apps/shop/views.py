from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.mail import send_mail
from django.http import HttpResponse

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


def send_email_view(request):
    send_mail(
        'test',  # Тема письма
        'привет. теперь ты будешь получать спам',  # Тело письма
        'dastiw1910@gmail.com',  # Адрес отправителя
        ['edilbekova_aiperi@mail.ru', 'urmatovnaa05@gmail.com'],  # Список адресов получателей
        fail_silently=False,  # Если установлено значение True, ошибки отправки будут игнорироваться
    )
    return HttpResponse('Email sent successfully!')


