from django import  forms


class CheckOutForm(forms.Form):

    first_name = forms.CharField(
        label='نام',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    last_name = forms.CharField(
        label='نام خانوادگی',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    state = forms.CharField(
        label='استان',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    city = forms.CharField(
        label='شهر',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    street = forms.CharField(
        label='خیابان',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    apartment = forms.CharField(
        label='آپارتمان',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    zipcode = forms.CharField(
        label='کدپستی',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )

    phone = forms.CharField(
        label='شماره تماس',
        max_length=250,
        required=True,
        error_messages={
            'max_length': 'کارکتر های وارد شده بیش از حد مجاز است'
        }
    )