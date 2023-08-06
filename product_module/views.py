from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .models import *


# Create your views here.
class ProductView(TemplateView):
    template_name = "products.html"

class FindProduct(View):
    def get(self, request, product):
        pro = get_object_or_404(Product, slug=product)
        return render(request, 'pro.html', context={
            'pr': pro
        })