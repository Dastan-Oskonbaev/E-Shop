from django.urls import path

from .views import CartView, CartAddView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', CartAddView.as_view(), name='cart-add'),
]