from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("signup", views.RegisterView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogOutView.as_view(), name="log_out"),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name="activate_account"),
    path("forget-password", views.ForgetPasswordView.as_view(), name="forget-password"),
    path("reset-password/<active_code>", views.ResetPasswordView.as_view(), name="reset-password"),
]
