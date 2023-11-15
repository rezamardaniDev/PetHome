from django.shortcuts import render, redirect
from django.views import View

from order_module.models import Order, OrderCheckout, OrderDetail


class AdminOrderView(View):
    def get(self, request):
        orders = OrderCheckout.objects.select_related('order').select_related("user")
        return render(request, 'order-admin.html', context={
            'orders': orders,
        })


class AdminOrderDetailView(View):
    def get(self, request, pk):
        products = OrderDetail.objects.filter(order_id=pk).all()
        return render(request, 'checkout-admin.html', context={
            'products': products
        })


def sended(request, pk):
    obj: OrderCheckout = OrderCheckout.objects.get(order_id=pk)
    obj.sended = True
    obj.save()

    return redirect('panel:order-admin')


def cancel(request, pk):
    obj: OrderCheckout = OrderCheckout.objects.get(order_id=pk)
    obj.sended = False
    obj.save()

    return redirect('panel:order-admin')
