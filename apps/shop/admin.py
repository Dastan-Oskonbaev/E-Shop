from django import forms
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Category, RatingStar, Rating, Product, Reviews, Specification


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


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
    inlines = [ReviewInLine, SpecificationInLine]
    save_on_top = True


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product')
    list_filter = ('product',)
    search_fields = ('product__name',)


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
