from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class ContactUsAdd(admin.ModelAdmin):
    list_display = ['subject', 'date']