from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'inventory']
    list_editable = ['unit_price']
    list_per_page = 10
    
    @admin.display(ordering=['inventory'])
    def inventory_status(self, product):
        if product.inventory < 20:
            return 'low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    
admin.site.register(models.Collection)

