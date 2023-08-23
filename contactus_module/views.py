from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsForm
from .models import ContactUs
from site_module.models import SiteSettings


class ContactUSView(View):
    def get(self, request):
        form = ContactUsForm()
        setting: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
        return render(request, "contact-us.html", context={
            'form':form,
            'settings': setting
        })
    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            new_message = ContactUs()
            new_message.email = form.cleaned_data.get('email')
            new_message.subject = form.cleaned_data.get('subject')
            new_message.message = form.cleaned_data.get('message')
            new_message.save()
            return redirect("home:main")
        else:
            form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, "contact-us.html", context={
            'form': form
        })