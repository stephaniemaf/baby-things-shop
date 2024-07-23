from django import template
from bag.models import Discount
from decimal import Decimal

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price,quantity):
    return price * quantity

@register.filter(name='calc_discount')
def calc_discount(total, discount_code):
    if discount_code:
        try:
            discount = Discount.objects.get(discount_code=discount_code, active=True, used=False)
            if discount.is_valid():
                # Ensure discount_amount is a Decimal and convert to Decimal if it's not
                discount_percentage = Decimal(discount.discount_amount)
                total = Decimal(total)  # Ensure total is also a Decimal
                discount_amount = total * (discount_percentage / Decimal('100.0'))
                total -= discount_amount
        except Discount.DoesNotExist:
            pass
    return total

@register.filter(name='final_amount')
def final_amount(value):
      return round(value, 2)
           

