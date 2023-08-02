from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LogInView(TemplateView):
    template_name = "login.html"


class SignUpView(TemplateView):
    template_name = "signup.html"


class ForgetPasswordView(TemplateView):
    template_name = "forget-password.html"


class ResetPasswordView(TemplateView):
    template_name = "reset-password.html"
