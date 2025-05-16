from django.contrib import admin
from .models import *

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu')
    list_filter = ('menu',)
    search_fields = ('name', 'menu__name')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'is_bestseller')
    list_filter = ('brand', 'category', 'is_bestseller')
    search_fields = ('title', 'brand__name', 'category__name')
    raw_id_fields = ('brand', 'category')