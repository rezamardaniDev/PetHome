import json
from django.conf import settings
import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from jdatetime import datetime

from .forms import CheckOutForm
from .models import OrderCheckout

from order_module.models import Order, OrderDetail
from product_module.models import Product


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

MERCHANT = '41af5198-62bc-4c31-af3a-424f4e73ec70'
# amount = 20000
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
phone = '09035913296'
#
CallbackURL = 'http://127.0.0.1:8000/order/verify'

def request_payment(request):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()

    if total_price == 0:
        return redirect(reverse('user:cart'))
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": total_price,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    try:
        response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response

    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify_payment(request):
    authority = request.GET['Authority']
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()

    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": total_price,
        'Authority': authority,

    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}

    res = requests.post(ZP_API_VERIFY, data=data, headers=headers)
    if res.status_code == 200:
        response = res.json()

        if response['Status'] == 100:
            current_order.is_paid = True
            current_order.save()
            return redirect(reverse('user:dashboard'))

    return HttpResponse('موفق نبود')


def add_product_to_order(request):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))

    if count < 1:
        return JsonResponse({
            'status': 'invalid count'
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(user_id=request.user.id, is_paid=False)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()
            return JsonResponse({
                'status': 'success'
            })


        else:
            return JsonResponse({
                'status': 'not found product'
            })
    else:
        return JsonResponse({
            'status': 'user is not login',
        })


class CheckOutView(View):
    def get(self, request):
        checkout_form = CheckOutForm()
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(
            user_id=request.user.id,
            is_paid=False)
        total_amoutn = 0

        for order_detail in current_order.orderdetail_set.all():
            total_amoutn += order_detail.product.price * order_detail.count

        return render(request, "checkout.html", context={
            'order': current_order,
            'sum': total_amoutn,
            ' checkout_form':  checkout_form
        })

    def post(self, request):
        checkout_form = CheckOutForm(request.POST)
        if checkout_form.is_valid():
            new_checkout: OrderCheckout = OrderCheckout()

            new_checkout.user = request.user
            new_checkout.order = Order.objects.filter(user=request.user).first()
            new_checkout.first_name = checkout_form.cleaned_data.get('first_name')
            new_checkout.last_name = checkout_form.cleaned_data.get('last_name')
            new_checkout.state = checkout_form.cleaned_data.get('state')
            new_checkout.city = checkout_form.cleaned_data.get('city')
            new_checkout.street = checkout_form.cleaned_data.get('street')
            new_checkout.apartment = checkout_form.cleaned_data.get('apartment')
            new_checkout.zipcode = checkout_form.cleaned_data.get('zipcode')
            new_checkout.phone = checkout_form.cleaned_data.get('phone')
            new_checkout.sended = False

            new_checkout.save()
            return redirect(reverse('order:request_payment'))
        else:
            checkout_form.add_error('phone', 'مشکلی در پرداخت پیش اومده')

        return render(request, "checkout.html", context={
            'checkout_form': checkout_form,
            'sum': 0
        })
