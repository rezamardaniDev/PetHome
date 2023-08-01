from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ProductView(TemplateView):
    template_name = "products.html"
