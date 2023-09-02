from django.shortcuts import render
from django.views import View

from order_module.models import OrderDetail, Order, OrderCheckout

class AdminOrderView(View):
    def get(self, request):
        order = OrderCheckout.objects.filter(order__is_paid=True)
        return render(request, 'order-admin.html', context={
            'order': order,
        })

class AdminCheckoutView(View):
    def get(self, request, order_id):
        current_order, created = Order.objects.get_or_create(id=order_id, is_paid=True)
        detail = current_order.orderdetail_set.all()

        checkout_detiail: OrderCheckout = OrderCheckout.objects.filter(order_id=order_id).first()

        return render(request, 'checkout-admin.html', context={
            'detail': detail,
            'check': checkout_detiail
        })


