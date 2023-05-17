from django.urls import path

from .views import CartView, CartAddView, RemoveFromCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart-add'),
    # path('remove_from_cart/<int:cart_item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
]