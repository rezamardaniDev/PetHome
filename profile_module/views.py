from django.shortcuts import render
from django.views.generic import TemplateView
from account_module.models import User


# Create your views here.
class UserProfileView(TemplateView):
    template_name = "user_profile.html"

