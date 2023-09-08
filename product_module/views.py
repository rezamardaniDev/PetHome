from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from .forms import CommentForm
from .models import Product, ProductCategory, ProductComment


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


# class ProductDetailView(View):
#     def get(self, request, product_id):
#         product = Product.objects.filter(is_active=True, id=product_id).first()
#         comments = product.comments.all()
#         return render(request, 'product_detail.html', context={
#             'product': product,
#             'comments': comments
#         })
#
#     def post(self, request, product_id):
#         comment_form: CommentForm = CommentForm(request.POST)
#         product: Product = Product.objects.filter(is_active=True, id=product_id).first()
#         user = request.user
#         if comment_form.is_valid():
#             new_comment = ProductComment()
#             new_comment.message = comment_form.cleaned_data.get('message')
#             new_comment.user = user
#             new_comment.product = product
#             new_comment.save()
#             return redirect('products:products_detail', product.id)
#         else:
#             comment_form.add_error('message', 'مشکلی در ثبت کامنت شما پیش آمده است')
#         return render(request, 'product_detail.html', context={
#             'product': product
#         })
#

def product_categories_component(request):
    product_categories: ProductCategory = ProductCategory.objects.filter(is_active=True)[0:3]

    return render(request, 'component/product_categories_component.html', context={
        'categories': product_categories
    })


class ProductDetailView(View):
    def get(self, request, product_id):
        product = Product.objects.filter(is_active=True, id=product_id).first()
        new_product: Product = Product.objects.filter(is_active=True).order_by('price')[0:4]
        comments = product.comments.all().order_by('-create_date')

        comment_message = request.GET.get('message')

        if request.GET:
            new_comment = ProductComment()
            new_comment.message = comment_message
            new_comment.user = request.user
            new_comment.product = product
            if comment_message:
                new_comment.save()

            return render(request, 'comment_product.html', context={
                'product': product,
                'comments': comments,
                'product_new': new_product
            })

        return render(request, 'product_detail.html', context={
            'product': product,
            'comments': comments,
            'product_new': new_product
        })
