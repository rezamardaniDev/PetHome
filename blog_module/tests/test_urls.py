from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog_module.views import *


class TestUrls(SimpleTestCase):
    def test_blog_list(self):
        url = reverse('blog:blog_list')
        self.assertEqual(resolve(url).func.view_class, BlogListView)

    def test_blog_detail(self):
        url = reverse('blog:blog_detail', args=(1,))
        self.assertEqual(resolve(url).func.view_class, BlogDetailView)
