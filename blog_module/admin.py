from django.contrib import admin
from .models import BlogCategory, Blog, BlogComment, BlogVisit


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'created_date', 'is_active']
    list_editable = ['is_active']

    def save_model(self, request, obj: Blog, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)

@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'is_read']

@admin.register(BlogVisit)
class BlogVisitAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']



admin.site.register(BlogCategory)
