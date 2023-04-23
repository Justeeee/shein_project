from django.contrib import admin

from apps.models import Product, Category, SubCategory

from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from apps.models.comments import Comment, CommentImages
from apps.models.product import ProductImages


# @admin.register(ProductImages)
class ProductImagesTabularInline(TabularInline):
    model = ProductImages
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = ('slug',)
    inlines = (ProductImagesTabularInline,)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    search_fields = ['name']
    list_display = ['slug', 'name', 'id']
    exclude = ('slug',)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(parent=None)


@admin.register(SubCategory)
class SubCategoryAdmin(ModelAdmin):
    search_fields = ['name']
    list_display = ['slug', 'name', 'id']
    exclude = ('slug',)

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(parent=None)


class CommentImageTabularInline(TabularInline):
    model = CommentImages
    extra = 1


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    exclude = ('updated_at',)
    inlines = [CommentImageTabularInline]