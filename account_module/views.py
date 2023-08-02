from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView
from .forms import SignUpForm
from .models import User


# Create your views here.
def login(request):
    return render(request, 'login.html', {})


class SignUpView(TemplateView):
    def get(self, request):
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            user_password = form.cleaned_data['password']
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                form.add_error('email', 'این ایمیل از قبل ثبت شده است')
            else:
                new_user = User(
                    email=user_email,
                    emal_active_code=get_random_string(22),
                    username=form.cleaned_data['email'][0:5]
                )
                new_user.set_password(user_password)
                new_user.save()
                return redirect("home:main")
        context = {
            'form': form
        }

        return render(request, 'signup.html', context)


class ForgetPasswordView(TemplateView):
    template_name = "forget-password.html"


class ResetPasswordView(TemplateView):
    template_name = "reset-password.html"
