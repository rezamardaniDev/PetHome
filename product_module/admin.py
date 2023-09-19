from django.contrib import admin
from .models import Product, ProductCategory, ProductComment


def zero_counter(modeladmin, request, queryset):
    rows_update = queryset.update(count=0)
    if rows_update == 1:
        message_bit = "محصول ناموجود شد"
    else:
        message_bit = "محصولات ناموجود شدند"
    modeladmin.message_user(request, "%s " % message_bit)


zero_counter.short_description = "ناموجود کردن"


def more_counter(modeladmin, request, queryset):
    rows_update = queryset.update(count=10)
    if rows_update == 1:
        message_bit = "محصول موجود شد"
    else:
        message_bit = "محصولات موجود شدند"
    modeladmin.message_user(request, "%s " % message_bit)


more_counter.short_description = "موجود کردن"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'count', 'is_active']
    list_editable = ['is_active', 'count']
    actions = [zero_counter, more_counter]


@admin.register(ProductComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'is_read']


admin.site.register(ProductCategory)
