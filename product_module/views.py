from django.shortcuts import render
from django.views.generic import ListView, View
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Product, ProductCategory, ProductComment
from .serializers import ProductSerializer


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


@api_view(['GET', 'POST'])
def product_all(request):
    if request.method == 'GET':
        products = Product.objects.filter(is_active=True).all()
        products_serialized = ProductSerializer(products, many=True)
        return Response(products_serialized.data, status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    else:
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)

class ProductApiListView(APIView):
    def get(self, request: Request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)


