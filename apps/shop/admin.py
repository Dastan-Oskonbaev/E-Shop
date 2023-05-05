from django import forms
from django.contrib import admin

from django.utils.safestring import mark_safe
from modeltranslation.translator import TranslationOptions

from .models import Category,  RatingStar, Rating, Product,  Reviews


from modeltranslation.admin import TranslationAdmin


class ProductAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label=' Описание')
    description_en = forms.CharField(label=' Описание')

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("title", "category", "url", )
#     list_filter = ("category", )
#     search_fields = ("title", "category__name")
#     inlines = [ReviewInLine]
#     save_on_top = True
#     save_as = True
#     form = ProductAdminForm
#     readonly_fields = ("get_image",)
#     fieldsets = (
#         (None, {
#             "fields": ('title', "description", ("poster", "get_image"))
#         }),
#         (None, {
#             "fields": (("country"), 'category')
#         }),
#         ("Options", {
#             "fields": (("url", ),)
#         }),
#     )
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')
#
#     def unpublish(self, request, queryset):
#         """Снять с публикации"""
#         row_update = queryset.update()
#         if row_update == 1:
#             message_bit = "1 запись была обновлена"
#         else:
#             message_bit = f"{row_update} записей были обновлены"
#         self.message_user(request, f"{message_bit}")
#
#     def publish(self, request, queryset):
#         """Опубликовать"""
#         row_update = queryset.update(draft=False)
#         if row_update == 1:
#             message_bit = "1 запись была обновлена"
#         else:
#             message_bit = f"{row_update} записей были обновлены"
#         self.message_user(request, f"{message_bit}")
#
#     publish.short_description = "Опубликовать"
#     # publish.allowed_permissions = ('change', )
#
#     unpublish.short_description = "Снять с публикации"
#     unpublish.allowed_permissions = ('change',)
#
#     get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'product', 'id')
    readonly_fields = ('name', 'email')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'product', 'ip')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # list_display = ('star', 'product', 'ip')


admin.site.register(RatingStar)

admin.site.site_title = 'E Shop'
admin.site.site_header = 'E Shop'
