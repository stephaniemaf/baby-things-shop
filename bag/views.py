
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from django.contrib import messages
from products.models import Product

def shop_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):

    try:
        bag = request.session.get('bag', {})
        if item_id in bag:
            del bag[item_id]
            request.session['bag'] = bag 
            return HttpResponse(status=200)
        else:
            return HttpResponse(status = 404)
    except Exception as e:
        return HttpResponse(status=500)

        


def adjust_bag(request, item_id):
    """ Add aproduct to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
         bag[item_id] = bag.get(item_id, 0) + quantity
    else:
        bag.pop(item_id, None)

    request.session['bag'] = bag
    return redirect(reverse('shop_bag'))