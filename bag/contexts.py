from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product
from bag.models import Discount  

""" making context availble threw entire aplication"""

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    discount_code = request.session.get('discount_code', '') 

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    discount_amount = Decimal('0.00')
    if discount_code:
        try:
            discount = Discount.objects.get(discount_code=discount_code, active=True, used=False)
            if discount.is_valid():
                discount_percentage = Decimal(discount.discount_amount)
                discount_amount = total * (discount_percentage / 100)
                total -= discount_amount
        except Discount.DoesNotExist:
       
            pass

    # Calculate delivery cost
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    standard_delivery_percentage = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE) / 100
    delivery = Decimal('0.00')
    if total < free_delivery_threshold:
        delivery = total * standard_delivery_percentage

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'subtotal': total,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'discount_code': discount_code,
        'discount_amount': discount_amount,  # Include discount amount if needed
    }

    return context