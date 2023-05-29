from django.db import models

from apps.accounts.models import User
from apps.shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    total_price = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f' Заказ {self.user.name} '

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f' Количество : {self.product} * {self.quantity}'

    class Meta:
        verbose_name = "Заказанный продукт"
        verbose_name_plural = "Заказанные продукты"


