from django import forms


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)