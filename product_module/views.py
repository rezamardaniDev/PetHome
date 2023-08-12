from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Product, ProductCategory


class ProductView(ListView):
    template_name = "products.html"
    model = Product
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True).all()
        context['products'] = Product.objects.filter(is_active=True).all()
        return context

class ProductDetailView(View):
    def get(self, request, product_slug):
        product = Product.objects.filter(is_active=True, slug=product_slug).first()

        return render(request, 'product_detail.html', context=
        {'product': product}
                      )
