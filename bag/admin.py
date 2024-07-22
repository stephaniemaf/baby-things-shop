from django.contrib import admin
from .models import Discount

# Register your models here.
class DiscountAdmin(admin.ModelAdmin):
    model = Discount
    list_display = (
        'discount_code',
        'active',       
    )
    search_fields = ['Discount Code',]

admin.site.register(Discount, DiscountAdmin)
