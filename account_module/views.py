from django.contrib.auth import login, logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import TemplateView

from utils.email_service import send_email
from .forms import RegisterForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from .models import User


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
                send_email('فعالسازی حساب', new_user.email, {'user': new_user}, 'emails/active_account.html')
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
                return redirect(reverse('home:main'))
            else:
                HttpResponse("your account is activated")
        raise Http404


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user: User = User.objects.filter(email__iexact=form.cleaned_data.get('email')).first()
            if user is not None:
                if not user.is_active:
                    form.add_error('email', 'حساب کاربری شما فعال نشده است، لطفا با پشتیبانی در تماس باشید')
                else:
                    is_password_correct = user.check_password(form.cleaned_data.get('password'))
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse("user:dashboard"))
                    else:
                        form.add_error('email', 'ایمیل یا پسورد اشتباه است')
            else:
                form.add_error('email', 'لطفا ابتدا ثبت نام کنید')
        else:
            form.add_error('email', 'خطایی هنگام ورود رخ داد')

        return render(request, 'login.html', context={
            'form': form,
        })


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("home:main")


class ForgetPasswordView(View):
    def get(self, request):
        form = ForgetPasswordForm()
        return render(request, "forget-password.html", context={
            'form': form
        })

    def post(self, request):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email__iexact=form.cleaned_data.get('email')).first()
            if user is not None:
                if user.is_active:
                    send_email('بازیابی رمز عبور', user.email, {'user': user}, 'emails/reset_password.html')
                    return redirect('account:login')
                else:
                    form.add_error('email', 'حساب کاربری فعال نشده')
            else:
                form.add_error('email',
                               'همچین کاربری یافت نشد... دوباره امتحان کنید یا در سایت لاگین کنید')
        else:
            form.add_error('email', 'خطایی در تکمیل فرم رخ داده')

        return render(request, "forget-password.html", context={
            'form': form
        })


class ResetPasswordView(View):
    def get(self, request, active_code):
        user = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('account:login'))
        else:
            form = ResetPasswordForm()
        return render(request, "reset-password.html", context={
            'form': form,
            'user': user
        })

    def post(self, request, active_code):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return redirect(reverse('account:login'))

            user.set_password(form.cleaned_data.get('password'))
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('account:login'))
        else:
            raise Http404

        return render(request, "reset-password.html", context={
            'form': form,
            'user': user
        })
