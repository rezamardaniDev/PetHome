
from django.contrib import admin
from django.urls import path, include
import home_module, product_module, account_module

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_module.urls", namespace="home")),
    path("products/", include("product_module.urls", namespace="products")),
    path("account/", include("account_module.urls", namespace="account"))
]
