from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.ProductListViewSetApiView)

app_name = "products"

urlpatterns = [
    path('', views.ProductView.as_view(), name="products_list"),
    path('api', views.product_all),
    path('api/<product_id>', views.product_detail_api),
    path('cbv', views.ProductApiListView.as_view()),
    path('cbv/<product_id>', views.ProductApiDetailView.as_view()),
    path('generics', views.ProductListGenericView.as_view()),
    path('generics/<pk>', views.ProductDetailGenericView.as_view()),
    path('mixin', views.ProductListMixinApiView.as_view()),
    path('mixin/<pk>', views.ProductDetailMixinApiView.as_view()),
    path('viewset/', include(router.urls)),
    path('<slug:product_id>', views.ProductDetailView.as_view(), name="products_detail"),
    path('cut/<str:category>', views.ProductView.as_view(), name="products_list_category"),

]
