from django.test import TestCase, Client
from django.urls import reverse


class TestBlog(TestCase):
    def setUp(self):
        self.client = Client()

    def test_blog_list(self):
        response = self.client.get(reverse('blog:blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_list.html')