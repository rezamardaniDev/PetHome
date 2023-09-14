from django.shortcuts import render
from account_module.models import User
from product_module.models import Product
from blog_module.models import Blog
from order_module.models import Order
from .serializer import *

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class UsersListGenericView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductListGenericView(ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True).all()
    serializer_class = ProductSerializer


class ProductDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(is_active=True).all()
    serializer_class = ProductSerializer


class BlogListGenericView(ListCreateAPIView):
    queryset = Blog.objects.filter(is_active=True).all()
    serializer_class = BlogSerializer


class BlogDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(is_active=True).all()
    serializer_class = BlogSerializer


class OrderListGenericView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
