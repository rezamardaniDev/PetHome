from django.test import SimpleTestCase
from django.urls import resolve, reverse
from account_module.views import *


class TestUrls(SimpleTestCase):
    def test_signup(self):
        url = reverse('account:signup')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_login(self):
        url = reverse('account:login')
        self.assertEqual(resolve(url).func.view_class, LoginView)

    def test_logout(self):
        url = reverse('account:log_out')
        self.assertEqual(resolve(url).func.view_class, LogOutView)

    def test_activate_account(self):
        url = reverse('account:activate_account', args=('fnvie8gaWq',))
        self.assertEqual(resolve(url).func.view_class, ActivateAccountView)

    def test_forget_password(self):
        url = reverse('account:forget-password')
        self.assertEqual(resolve(url).func.view_class, ForgetPasswordView)

    def test_reset_password(self):
        url = reverse('account:reset-password', args=('fegsgeg',))
        self.assertEqual(resolve(url).func.view_class, ResetPasswordView)
