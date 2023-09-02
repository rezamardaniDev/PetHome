from django.shortcuts import render
from django.views import View

from order_module.models import OrderDetail, Order, OrderCheckout


# Create your views here.
class AdminOrderView(View):
    def get(self, request):
        order = OrderCheckout.objects.filter(order__is_paid=True)
        print(order)
        return render(request, 'order-admin.html', context={
            'order': order,
        })

