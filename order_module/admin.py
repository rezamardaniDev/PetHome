from django.contrib import admin
from . import models


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_paid']


@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order']


@admin.register(models.OrderCheckout)
class OrderCheckoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'sended']


admin.site.register(models.Discount)

admin.site.register(models.UserDescount)
