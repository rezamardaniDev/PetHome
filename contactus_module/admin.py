from django.contrib import admin
from .models import ContactUs
# Register your models here.
@admin.register(ContactUs)
class ContactUsAdd(admin.ModelAdmin):
    list_display = ['subject', 'date']