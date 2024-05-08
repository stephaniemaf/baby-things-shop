from django.contrib import admin
from .models import Delivery

# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'order',
        'status',
        'order_date',
        'is_paid',
    )

admin.site.register(Delivery, DeliveryAdmin)
