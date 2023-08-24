from django.http import HttpResponse
from django.shortcuts import render

def add_product_to_order(request):
    print(request.GET)
    product_id = request.GET.get('product_id')
    product_count = request.GET.get('count')
    print(f'productId={product_id}, count={product_count}')
    return HttpResponse('done')