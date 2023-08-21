from django import forms
from account_module.models import User


class EditeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'profile_image']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label="رمز عبور فعلی",
        widget=forms.TextInput(),
        error_messages={
            'required': 'رمزعبور خود را وارد کنید'
        }
    )
    new_password = forms.CharField(
        label="رمز عبور جدید",
        widget=forms.TextInput(),
        error_messages={
            'required': 'رمزعبور خود را مجددا وارد کنید'
        }
    )
    confirm_password = forms.CharField(
        label="تایید رمز عبور ",
        widget=forms.TextInput(),
        error_messages={
            'required': 'رمزعبور خود را مجددا وارد کنید'
        }
    )
