from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from product_module.views import *
from profile_module.forms import EditeProfileForm
from account_module.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_dashboard = reverse("user:dashboard")
        self.user_edite = reverse("user:edit_profile")

    def test_user_dashboard(self):
        response = self.client.get(self.user_dashboard)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_profile.html")

    def test_user_edite_profile_get(self):
        response = self.client.get(self.user_edite)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edite_profile.html")
        self.failUnless(response.context['edit_form'], EditeProfileForm)

    def test_user_edite_profile_POST_valid(self):
        response = self.client.post(self.user_edite, data={
            'first_name': 'reza',
            'last_name': 'mardani',
            'address': 'shiraz',
            'phone_number': '0788'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('user:edit_profile'))
        self.assertTrue(User.objects.count(), 0)

    def test_user_edite_profile_POST_invalid(self):
        response = self.client.post(self.user_edite, data={
            'first_name': 'reza',
            'last_name': 'mardani',
            'address': 'shiraz',
            'phone_number': ''
        })
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['edit_form'].is_valid())
