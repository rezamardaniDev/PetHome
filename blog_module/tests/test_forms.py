from django.test import TestCase
from blog_module.forms import *


class TestCommentForm(TestCase):

    def test_comment_valid(self):
        form = CommentForm(data={
            'message': 'Hello'
        })
        self.assertTrue(form.is_valid())

    def test_comment_empty(self):
        form = CommentForm(data={
            'message': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
