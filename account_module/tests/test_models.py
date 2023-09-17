from django.test import TestCase
from account_module.models import User
from model_bakery import baker


class TestUser(TestCase):
    def test_user_str(self):
        user = baker.make(User, first_name='reza', last_name='mardani')
        self.assertEqual(str(user), 'reza mardani')
