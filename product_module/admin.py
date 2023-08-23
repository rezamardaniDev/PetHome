from django.contrib import admin
from .models import Product, ProductCategory, ProductComment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'category','count', 'is_active']
    list_editable = ['is_active', 'count']

@admin.register(ProductComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'is_read']

admin.site.register(ProductCategory)