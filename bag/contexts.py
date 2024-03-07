from django.conf import settings
from decimal import Decimal
""" making context availble threw entire aplication"""

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    delivery = total * Decimal(settings.STARNDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total 
    context = {
        'bag_items' : bag_items,
        'total' : total,
        'product_count' : product_count,
        'grand_total' : grand_total,
    }

    return context