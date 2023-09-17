from django.test import TestCase, Client
from django.urls import reverse
from account_module.models import User
from account_module.forms import RegisterForm


class TestUserRegister(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('account:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.failUnless(response.context['form'], RegisterForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('account:signup'), data={
            'first_name': 'raza',
            'last_name': 'mardani',
            'email': 'test@example.com',
            'phone_number': 121,
            'password': 'ffff',
            'confirm_password': 'ffff',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:main'))
        self.assertEqual(User.objects.count(), 1)

    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse('account:signup'), data={
            'first_name': 'raza',
            'last_name': 'mardani',
            'email': 'testexample.com',
            'phone_number': 121,
            'password': 'ffff',
            'confirm_password': 'ffff',
        })
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(form=response.context['form'], field='email', errors=['پست الکترونیکی صحبح وارد کنید.', 'خطایی در ثبت نام رخ داده است'])

