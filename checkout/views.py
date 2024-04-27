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
    }
    return render(request, template, context)
   