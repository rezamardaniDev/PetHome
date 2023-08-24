from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add_to_order')
]