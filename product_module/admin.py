from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price', 'productcategory','count', 'is_active']
    list_editable = ['is_active', 'count']
admin.site.register(ProductCategory)