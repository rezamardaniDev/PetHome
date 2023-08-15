from django.urls import path
from . import views

app_name = "contact-us"

urlpatterns = [
    path("", views.ContactUSView.as_view(), name="contact-us")
]