from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Категория', max_length= 150)
    description = models.TextField('Описание', default='')
    url = models.SlugField(max_length=160, unique=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    title = models.CharField('Название', max_length=100, default='')
    description = models.TextField("Описание", default='')
    poster = models.ImageField('Постер', upload_to='shop/', default='')
    # year = models.SmallIntegerField('Дата выхода', default='')
    country = models.CharField('Страна', max_length=30, default='')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


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
