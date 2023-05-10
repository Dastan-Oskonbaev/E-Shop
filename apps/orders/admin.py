from django.contrib import admin

from apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'email', 'total', 'comment')
    list_filter = ('user', 'address', 'email', 'total', 'comment')
    search_fields = ('user', 'address', 'email',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'order')
    list_filter = ('product', 'quantity', 'order')