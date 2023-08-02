from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login", views.login, name="login"),
    path("forget-password", views.ForgetPasswordView.as_view(), name="forget-password"),
    path("reset-password", views.ResetPasswordView.as_view(), name="reset-password"),
]