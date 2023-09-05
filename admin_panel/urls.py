from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('orders', views.AdminOrderView.as_view(), name='order-admin'),
    path('checkouts/<order_id>', views.AdminCheckoutView.as_view(), name='checkout-admin'),
]