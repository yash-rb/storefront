from typing import Any
from django.db.models import Count
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models
from django.utils.html import format_html, urlencode
from django.urls import reverse
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    
    def collection_title(self, product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 20:
            return 'low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    
    @admin.display(ordering='orders_count') 
    def orders_count(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id':str(customer.id)
            })
               )
        orders_represent = f"{customer.orders_count} Orders" if customer.orders_count >0 else 0
        return format_html('<a href="{}">{}</a>', url, orders_represent)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(orders_count=Count('order'))
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at','customer', ]
    list_per_page = 10
    list_select_related = ['customer']
    
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
   
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            })
            )
        return format_html('<a href="{}">{}</a>',url, collection.products_count)
         

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
            
        )

