from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.ProductView.as_view(), name="products_list")
]