from django.contrib import admin
from .models import BlogCategory, Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'auther', 'created_date', 'is_active']
    list_editable = ['is_active']

admin.site.register(BlogCategory)
