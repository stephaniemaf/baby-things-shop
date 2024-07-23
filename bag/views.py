
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product
from django.http import JsonResponse
from .forms import DiscountCodeForm
from bag.contexts import bag_contents

def shop_bag(request):
    return render(request, 'bag/bag.html')


def add_and_remove(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity',0))
    action = request.POST.get('action')
    redirect_url = request.POST.get('redirect_url')

    try:
        bag = request.session.get('bag', {})

        if action == 'add':
            if item_id in bag:
                bag[item_id] += quantity
            else:
                bag[item_id] = quantity
            messages.success(request, "Item has been added to your cart")

        elif action == 'remove':
            if item_id in bag:
                if bag[item_id] > quantity:
                    bag[item_id] -= quantity
                    messages.success(request, "Selected item removed from your cart")
                else:
                    bag.pop(item_id)
                    messages.success(request,"Item removed from your cart")
            else:
                messages.error(request, "Item is not in your cart")
        else:
            messages.error(request, "Invalid action")  
            return HttpResponse(status=500)

        request.session['bag'] = bag
        return redirect(redirect_url)

    except Exception as e:
            messages.error(request, "An error occurred while trying to update the item. Please contact us.")
            return HttpResponse(status=500)

def adjust_bag(request, item_id):
    print(f"Adjusting bag for item_id: {item_id}")  # Debugging line
    quantity = int(request.POST.get('quantity', 0))
    bag = request.session.get('bag', {})

    if quantity > 0:
         bag[item_id] = quantity
    else:
        bag.pop(item_id, None)

    request.session['bag'] = bag
    print(f"Updated bag: {bag}")  # Debugging line
    return redirect(reverse('shop_bag'))


def empty_bag(request):
    if request.method == 'POST':
        # Clear the cart by removing the 'bag' session data
        request.session['bag'] = {}
        return redirect(reverse('shop_bag'))  # Redirect to the shopping bag page
    else:
        return redirect(reverse('shop_bag'))  # Handle non-POST requests

def apply_discount(request):
    if request.method == 'POST':
        form = DiscountCodeForm(request.POST)
        if form.is_valid():
            discount_code = form.cleaned_data['discount_code']
            request.session['discount_code'] = discount_code
            messages.success(request, "Discount code applied.")
        else:
            messages.error(request, "Invalid discount code.")
        return redirect('shop_bag')