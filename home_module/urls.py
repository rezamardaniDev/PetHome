from django.urls import path
from . import views

app_name = "home_module"

urlpatterns = [
    path('', views.HomeView.as_view(), name="main")
]