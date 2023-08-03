from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label="نام",
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        widget=forms.TextInput()
    )
    phone_number = forms.IntegerField(
        label="شماره تماس",
        widget=forms.NumberInput()
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput()
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.TextInput()
    )
    confirm_password = forms.CharField(
        label="تکرار پسورد",
        widget=forms.TextInput()
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("رمز عبور های وارد شده یکسان نیستند")


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(),
        error_messages={
            'required': 'ایمیل خود را وارد کنید'
        }
    )

    password = forms.CharField(
        label="پسورد",
        widget=forms.TextInput(),
        error_messages={
            'required': 'رمزعبور خود را وارد کنید'
        }
    )