from django.urls import path

from .views import OrderView, RemoveFromOrderView

urlpatterns = [
    path('', OrderView.as_view(), name='order'),
    path('remove/<int:product_id>/', RemoveFromOrderView.as_view(), name='remove-from-order'),
]