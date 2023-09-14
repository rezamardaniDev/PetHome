from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('api/users', views.UsersListGenericView.as_view(), name='user-list-generic'),
    path('api/users/<pk>', views.UsersListGenericView.as_view(), name='user-detail-generic'),
    path('api/products', views.ProductListGenericView.as_view(), name='products-list-generic'),
    path('api/products/<pk>', views.ProductDetailGenericView.as_view(), name='products-detail-generic'),
    path('api/blog', views.BlogListGenericView.as_view(), name='products-list-generic'),
    path('api/blog/<pk>', views.ProductDetailGenericView.as_view(), name='products-detail-generic'),
]
