from django.http import JsonResponse

from order_module.models import Order, OrderDetail
from product_module.models import Product


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
                new_detail = OrderDetail(order_id=current_order.id,  product_id=product_id, count=count)
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