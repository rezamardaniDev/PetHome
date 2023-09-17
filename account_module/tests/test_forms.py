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
