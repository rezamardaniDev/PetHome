from django.urls import path
from . import views
app_name = 'api'

urlpatterns = [
    path('api/users', views.UsersListGenericView.as_view(), name='user-list-generic'),
    path('api/users/<pk>', views.UsersListGenericView.as_view(), name='user-detail-generic'),
]