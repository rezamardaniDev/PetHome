from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import TemplateView
from .forms import RegisterForm
from .models import User


class LoginView(TemplateView):
    template_name = "login.html"


class RegisterView(TemplateView):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'signup.html', context={
            'form': form
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            exist_user: User & bool = User.objects.filter(email__iexact=form.cleaned_data.get('email')).exists()
            if not exist_user:
                new_user = User()
                new_user.first_name = form.cleaned_data.get('first_name')
                new_user.last_name = form.cleaned_data.get('last_name')
                new_user.email = form.cleaned_data.get('email')
                new_user.phone_number = form.cleaned_data.get('phone_number')
                new_user.username = form.cleaned_data.get('phone_number')
                new_user.set_password(form.cleaned_data.get('password'))
                new_user.email_active_code = get_random_string(72)
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


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('home:main'))
            else:
                HttpResponse("حساب کاربری شما فعال هست")
        raise Http404


class ForgetPasswordView(TemplateView):
    template_name = "forget-password.html"


class ResetPasswordView(TemplateView):
    template_name = "reset-password.html"
