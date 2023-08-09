from django import forms


class ContactUsForm(forms.Form):
    email = forms.CharField(
        label='ایمیل شما',
        max_length=300,
        required=True,
        error_messages={
            'max_length': 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'ایمیل معتبر...'
        })
    )

    subject = forms.CharField(
        label='موضوع پیام',
        max_length=300,
        required=True,
        error_messages={
            'max_length': 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.PasswordInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'موضوع پیام...'
        })
    )

    message = forms.CharField(
        label='متن پیام',
        max_length=300,
        required=True,
        error_messages={
            'max_length': 'تعداد کارکتر وارد شده بیش از حد مجاز میباشد'
        },
        widget=forms.Textarea(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'متن پیام...',
            'cols': 60,
            'rows': 9
        })
    )
