from django import forms
from .models import BlogComment


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)