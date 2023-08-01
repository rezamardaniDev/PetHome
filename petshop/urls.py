
from django.contrib import admin
from django.urls import path, include
import home_module

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_module.urls", namespace="home"))
]
