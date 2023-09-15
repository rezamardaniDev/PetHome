from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_module.urls", namespace="home")),
    path("products/", include("product_module.urls", namespace="products")),
    path("account/", include("account_module.urls", namespace="account")),
    path("contact-us/", include("contactus_module.urls", namespace="contact-us")),
    path("blog/", include("blog_module.urls", namespace="blog")),
    path("user/", include("profile_module.urls", namespace="user")),
    path("gallery/", include("gallery_module.urls", namespace="gallery")),
    path('order/', include("order_module.urls", namespace="order")),
    path('panel/', include("admin_panel.urls", namespace="panel")),
    path('', include("API.urls", namespace="api")),
    path('auth-token/', obtain_auth_token, name='generate_auth_token'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
