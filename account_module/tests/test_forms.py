from django.test import TestCase
from account_module.forms import RegisterForm
from account_module.models import User


class TestRegister(TestCase):
    def test_valid_data(self):
        form = RegisterForm(data={
            'first_name': 'reza',
            'last_name': 'mardani',
            'phone_number': 24554,
            'email': 'mardani@gmail.com',
            'password': '1234',
            'confirm_password': '1234'
        })
        self.assertTrue(form.is_valid())

    def test_empty_date(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)

    def test_on_match(self):
        form = RegisterForm(data={
            'first_name': 'reza',
            'last_name': 'mardani',
            'phone_number': 24554,
            'email': 'mardani@gmail.com',
            'password': '1234',
            'confirm_password': '123'
        })
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error)

    def test_email_exist(self):
        user = User.objects.create(
            username='ali',
            last_name='zare',
            phone_number=4455,
            email='test@exampl.com',
            password='1234',
        )
        form = RegisterForm(data={
            'first_name': 'reza',
            'last_name': 'mardani',
            'phone_number': 24554,
            'email': 'test@exampl.com',
            'password': '1234',
            'confirm_password': '1234'
        })
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))
