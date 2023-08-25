from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('dashboard', views.UserProfileView.as_view(), name='dashboard'),
    path('edit', views.UserEditProfile.as_view(), name='edit_profile'),
    path('change-passoword', views.ChangePasswordView.as_view(), name='change_password'),
    path('cart', views.user_basket, name='cart'),
    path('delete-order-detail', views.delete_order_detail, name='delete_order_detail_ajax'),
]