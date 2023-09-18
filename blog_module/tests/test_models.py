from django.test import TestCase
from blog_module.models import Blog, BlogComment
from model_bakery import baker


class TestBlog(TestCase):
    def setUp(self):
        self.blog = baker.make(Blog, title='post')

    def test_blog_str(self):
        self.assertEqual(str(self.blog), 'post')

 