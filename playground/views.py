from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem, Order


def say_hello(request):
    #Get all the products which are ordered and sort acc to title
    products = Product.objects.filter(id__in=
                                    OrderItem.objects.values('product_id').distinct()).order_by('title')
    #get products of last 5 orders" 
    orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    
    return render(request, 'hello.html', {'name': 'Yash', 'products':list(products), 'orders':list(orders)})

