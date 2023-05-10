from django import forms
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category, RatingStar, Rating, Product, Reviews,  Cart, CartItem, ProductImage, Specification


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


class SpecificationInLine(admin.TabularInline):
    model = Specification
    extra = 1


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'indented_title',
    )
    list_display_links = (
        'indented_title',
    )
    list_filter = ['parent']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "description")
    list_filter = ("name", "category", "price", "quantity", "description")
    search_fields = ("name", "category", "price", "quantity", "description")
    inlines = [ReviewInLine, SpecificationInLine, ProductImageInLine]
    save_on_top = True


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product')
    list_filter = ('product',)
    search_fields = ('product__name',)


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    list_filter = ('product',)
    search_fields = ('product__name',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity')
    list_filter = ('product', 'cart', 'quantity')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'product', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'product', 'ip')


admin.site.register(RatingStar)

admin.site.site_title = 'E Shop'
admin.site.site_header = 'E Shop'
