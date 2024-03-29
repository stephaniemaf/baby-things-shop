from django.contrib import admin
from .models import Category, Product, Customer, Delivery, Order_history


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'email',
    )

class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'address',
        'delivery_date',
    )

class Order_historyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'email',
        'order_total',
        'order_date',
        'quantity',
    )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(Order_history, Order_historyAdmin)

