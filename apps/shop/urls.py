from django.urls import path

from apps.shop import views
from apps.shop.views import cart_add, cart_remove, index, shop

urlpatterns = [
    path("", index, name='index'),
    path("shop/", shop, name='shop'),
    path("category/<int:category_id>", shop, name='category'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_remove, name='cart_remove'),

]
