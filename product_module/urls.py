from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.ProductView.as_view(), name="products_list"),
    path('api', views.product_all),
    path('cbv', views.ProductApiListView.as_view()),
    path('<slug:product_id>', views.ProductDetailView.as_view(), name="products_detail"),
    path('cut/<str:category>', views.ProductView.as_view(), name="products_list_category"),
    path('api/<product_id>', views.product_detail_api),
]
