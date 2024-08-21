from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product, OrderItem


def say_hello(request):
    #Get all the products which are ordered and sort acc to title
    products = Product.objects.filter(id__in=
                                    OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    
    return render(request, 'hello.html', {'name': 'Yash', 'products':list(products)})

