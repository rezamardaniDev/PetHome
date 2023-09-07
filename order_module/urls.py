from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add_to_order'),
    path('checkout', views.CheckOutView.as_view(), name='checkout'),
    path('request', views.request_payment, name='request_payment'),
    path('verify', views.verify_payment, name='verify_payment'),
    path('seccess', views.secces_payment_redirect, name='secces_payment_redirect'),
    path('unseccess', views.unsecces_payment_redirect, name='unsecces_payment_redirect')
]
