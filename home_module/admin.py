from django.contrib import admin

from home_module.models import AskQuestion


@admin.register(AskQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'question']