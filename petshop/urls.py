
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_module.urls", namespace="home")),
    path("products/", include("product_module.urls", namespace="products")),
    path("account/", include("account_module.urls", namespace="account")),
    path("contact-us/", include("contactus_module.urls", namespace="contact-us")),
    path("blog/", include("blog_module.urls", namespace="blog")),
    path("user/", include("user_module.urls", namespace="user")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)