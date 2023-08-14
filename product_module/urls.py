from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.ProductView.as_view(), name="products_list"),
    path('<slug:product_slug>',views.ProductDetailView.as_view(), name="products_detail"),
    path('cut/<str:category>', views.ProductView.as_view(), name="products_list_category"),
]