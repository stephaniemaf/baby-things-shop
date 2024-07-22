from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price,quantity):
    return price * quantity

@register.filter(name='calc_discount')
def calc_discount(subtotal, discount_code):
    if discount_code:
        try:
            discount = Discount.objects.get(discount_code=discount_code, active=True, used=False)
            if discount.is_valid():
                disocount_amount = discount.discount_amount
                return subtotal * (1 - disocunt_amount / 100.0)
        except Discount.DoesNotExist:
            messages.error("Discount code invalid or does not exist")
    return subtotal

@register.filter(name='final_amount')
def final_amount(value):
      return round(value, 2)
           

