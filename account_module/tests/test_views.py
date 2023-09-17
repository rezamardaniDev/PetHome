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
            'email_active_code': 'fdsfsdvewew',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:main'))
        self.assertEqual(User.objects.count(), 1)
