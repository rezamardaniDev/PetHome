from django import forms
from account_module.models import User


class EditeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'profile_image']

        widgets = {
            'profile_image': forms.ImageField(attrs={
                'class': 'form-control',
            })
        }