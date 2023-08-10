
from django.contrib import admin
from django.urls import path, include
import home_module, product_module, account_module, contactus_module
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home_module.urls", namespace="home")),
    path("products/", include("product_module.urls", namespace="products")),
    path("account/", include("account_module.urls", namespace="account")),
    path("contact-us/", include("contactus_module.urls", namespace="contact-us"))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)