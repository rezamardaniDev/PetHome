from django.contrib import admin
from .models import User


@admin.register(User)
class UserManager(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']
    list_editable = ['is_active', 'is_staff', 'is_superuser']
