from django.shortcuts import render
from django.views import View

from order_module.models import Order, OrderCheckout, OrderDetail


class AdminOrderView(View):
    def get(self, request):
        current_order: Order = Order.objects.filter(is_paid=True).all()
        return render(request, 'order-admin.html', context={
            'order': current_order,
        })

class AdminCheckoutView(View):
    def get(self, request, order_id):

        detail = Order.objects.filter(id=order_id).first()
        detailn = OrderDetail.objects.filter(order=detail)
        print(detailn)

        return render(request, 'checkout-admin.html', context={
            'detail': detail,
        })


