from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from product_module.models import Product


def add_product_to_order(request):
    print(request.GET)
    product_id = request.GET.get('product_id')
    product_count = request.GET.get('count')
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True).first()
        if product is not None:
            # get user open order
            # add product to order
            pass
    else:
        return JsonResponse({
            'status': 'user is not login',
        })