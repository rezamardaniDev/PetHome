from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView
from .forms import RegisterForm
from .models import User


# Create your views here.
def login(request):
    return render(request, 'login.html', {})


class RegisterView(TemplateView):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'signup.html', context={
            'form': form
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            exist_user: User & bool = User.objects.filter(email__iexact=form.cleaned_data.get('emai')).exists()
            if not exist_user:
                new_user = User()
                new_user.first_name = form.cleaned_data.get('first_name')
                new_user.last_name = form.cleaned_data.get('last_name')
                new_user.email = form.cleaned_data.get('email')
                new_user.phone_number = form.cleaned_data.get('phone_number')
                new_user.set_password(form.cleaned_data.get('password'))
                new_user.is_active = False
                new_user.is_staff = False
                new_user.is_superuser = False
                new_user.save()
                return redirect("home:main")
            else:
                form.add_error('email', 'این ایمیل از قبل ثبت شده است')
        else:
            form.add_error('email', 'خطایی در ثبت نام رخ داده است')
        return render(request, 'signup.html', context={
            'form': form
        })


class ForgetPasswordView(TemplateView):
    template_name = "forget-password.html"


class ResetPasswordView(TemplateView):
    template_name = "reset-password.html"
