from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.BlogListView.as_view(), name="blog_list"),
    path('<slug:post_id>', views.BlogDetailView.as_view(), name="blog_detail"),
    path('cat/<str:category>', views.BlogListView.as_view(), name="blog_list_category"),
]