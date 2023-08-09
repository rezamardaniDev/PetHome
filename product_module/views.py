from django.views.generic import TemplateView


class ProductView(TemplateView):
    template_name = "products.html"