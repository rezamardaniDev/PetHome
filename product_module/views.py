from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from .models import *


class ProductView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account:login')
    template_name = "products.html"

class FindProduct(View):
    def get(self, request, product):
        pro = get_object_or_404(Product, slug=product)
        return render(request, 'pro.html', context={
            'pr': pro
        })