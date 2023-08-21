from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Product, ProductCategory


class ProductView(ListView):
    template_name = "products.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        query = super(ProductView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query

class ProductDetailView(View):
    def get(self, request, product_id):
        product = Product.objects.filter(is_active=True, id=product_id).first()

        return render(request, 'product_detail.html', context=
        {'product': product}
                      )

    def post(self, request):
        ...

def product_categories_component(request):
    product_categories: ProductCategory = ProductCategory.objects.filter(is_active=True)[0:3]

    return render(request, 'component/product_categories_component.html', context={
    'categories': product_categories
    })
