from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Product, ProductCategory


class ProductView(ListView):
    template_name = "products.html"
    model = Product
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        query = super(ProductView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query

class ProductDetailView(View):
    def get(self, request, product_slug):
        product = Product.objects.filter(is_active=True, slug=product_slug).first()

        return render(request, 'product_detail.html', context=
        {'product': product}
                      )

def product_categories_component(request):
    product_categories: ProductCategory = ProductCategory.objects.filter(is_active=True)[0:3]

    return render(request, 'component/product_categories_component.html', context={
    'categories': product_categories
    })
