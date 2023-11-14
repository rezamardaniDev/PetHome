from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('orders', views.AdminOrderView.as_view(), name='order-admin'),
    path('detail/<pk>',views.AdminOrderDetailView.as_view(), name='order-admin-detail' )

]