from django.urls import path
from apps.shop.views import IndexView, ShopView, ProductDetailView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("shop/", ShopView.as_view(), name='shop'),
    path("category/<int:category_id>", ShopView.as_view(), name='category'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]
