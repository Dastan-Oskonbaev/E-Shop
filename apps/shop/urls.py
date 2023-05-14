from django.urls import path

from apps.shop import views
from apps.shop.views import cart_add, cart_remove, IndexView, ShopView, ProductDetailView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("shop/", ShopView.as_view(), name='shop'),
    path("category/<int:category_id>", ShopView.as_view(), name='category'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),

]
