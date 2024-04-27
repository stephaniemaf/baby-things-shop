from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .forms import OrderForm
# stop people adding slash to url and manually accessing the checkout 

def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request,'There is nothing in your cart right now')
        return redirct(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'strip_public_key': pk_test_51PA9dl01FZVkM9LpC0mO0p67kKgfgHriBkMn1FTlq2k583PxCKTGI3ga18j42dlnud1VCJvUU819sSURrBmwb6p400WsJQfRqP
    }
    return render(request, template, context)
   