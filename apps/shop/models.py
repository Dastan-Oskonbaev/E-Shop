from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    name = models.CharField(
        _('Название'),
        max_length=255,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )
    description = models.TextField(
        _('Описание'),
        max_length=500
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        order_insertion_by = ['name']


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('Категория'),

    )
    name = models.CharField(
        _('Название'),
        max_length=255
    )
    price = models.PositiveIntegerField(
        _('Цена')
    )
    quantity = models.PositiveIntegerField(
        _('Количество')
    )
    description = models.TextField(
        _('Описание'),
        max_length=500
    )
    image = models.ImageField(
        _('Изображение'),
        upload_to='product_images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Specification(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=100
    )
    value = models.CharField(
        _('Значение'),
        max_length=250
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Продукт'),
        related_name='specifications'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'Корзина {self.user}'
#
#
# class CartItem(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return f' Товары в корзине {self.user}'
#
#     def sum(self):
#         return self.product.price * self.quantity
#
#     def total_sum(self):
#         carts = CartItem.objects.filter(user=self.user)
#         return sum(cart.sum() for cart in carts)
#
#     def total_quantity(self):
#         carts = CartItem.objects.filter(user=self.user)
#         return sum(cart.quantity() for cart in carts)
#
#     class Meta:
#         verbose_name = "Товар в корзине"
#         verbose_name_plural = "Товары в корзине"
#

class RatingStar(models.Model):
    value = models.SmallIntegerField('Значение', default='1')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда Рейтинга"
        verbose_name_plural = "Звезды Рейтинга"
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звезда')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.star} - {self.product}'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Текст', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='родитель', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


