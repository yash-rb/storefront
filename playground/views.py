from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from store.models import Product


def say_hello(request):
    #better way to handle exception
    #first() return NONE if no object does not exist
    product = Product.objects.filter(pk=0).first()
    
    return render(request, 'hello.html', {'name': 'Yash'})

