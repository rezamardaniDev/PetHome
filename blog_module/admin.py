from django.contrib import admin
from .models import BlogCategory, Blog, BlogComment, BlogVisit


def active_post(modeladmin, request, queryset):
    rows_update = queryset.update(is_active=True)
    if rows_update == 1:
        message_bit = "پست فعال شد"
    else:
        message_bit = "پست ها فعال شدند"
    modeladmin.message_user(request, "%s " % message_bit)


active_post.short_description = 'فعال کردن مقالات'


def deactive_post(modeladmin, request, queryset):
    rows_update = queryset.update(is_active=False)
    if rows_update == 1:
        message_bit = "پست غیرفعال شد"
    else:
        message_bit = "پست های غیرفعال شدند"
    modeladmin.message_user(request, "%s " % message_bit)


deactive_post.short_description = "غیرفعال کردن مقالات"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'is_active']
    list_editable = ['is_active']
    actions = [active_post, deactive_post]

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
