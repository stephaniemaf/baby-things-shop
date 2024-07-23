from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.conf import settings
from bag.contexts import bag_contents
from .models import Order, OrderLineItem, Customer
from products.models import Product
from profiles.models import Delivery, UserProfile
from profiles.forms import UserProfileForm, DeliveryForm
from .forms import OrderForm, CustomerForm
from datetime import datetime
from decimal import Decimal
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
    standard_delivery_percentage = Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
    bag = request.session.get('bag', {})
    discount_code = request.session.get('discount_code', '')
    
    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order_date = datetime.now().date()
            #save infro to customer model on admin panel
            full_name = order_form.cleaned_data['full_name']
            email = order_form.cleaned_data['email']
            phone_number = order_form.cleaned_data['phone_number']

            return_customer = Customer.objects.filter(email=email).first()

            if return_customer:
                customer = return_customer
            else:
                customer = Customer.objects.create(
                    name=full_name,
                    email=email,
                    phone_number=phone_number,
                
            )
            full_name = order_form.cleaned_data['full_name']
            phone_number = order_form.cleaned_data['phone_number']
            street_address1 = order_form.cleaned_data['street_address1']
            town_or_city = order_form.cleaned_data['town_or_city']
            county = order_form.cleaned_data['county']
            country = order_form.cleaned_data['country']
            postcode = order_form.cleaned_data['postcode']
            
            user = request.user
            delivery = Delivery.objects.create(
                name = full_name,
                order=user,
                order_date=order_date,
                phone_number=phone_number,
                street_address1=street_address1,
                town_or_city=town_or_city,
                county =county, 
                country=country,
                postcode=postcode,
                is_paid = True
            )

            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        quantity=item_data.get('quantity')
                        if quantity is not None:
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                            )
                            order_line_item.save()
                        else:
                            messages.error(request, "No quantity data for product in your bag "
                            "please call us for assistance")
                            order.delete()
                            return redirect(reverse('shop_bag'))
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('shop_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        subtotal = Decimal(current_bag['subtotal'])
        discount_amount = Decimal(current_bag['discount_amount'])
        delivery = Decimal('0.00')

        if subtotal >= free_delivery_threshold:
            delivery = 0
        else:
            delivery = round(subtotal * (standard_delivery_percentage / Decimal('100')), 2)

        grand_total = subtotal - discount_amount + delivery
        stripe_total = round(grand_total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'subtotal': subtotal,
        'discount_amount': discount_amount,
        'delivery': delivery,
        'grand_total': grand_total,

    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    if save_info:
        profile_data = {
            'default_phone_number': order.phone_number,
            'default_country': order.country,
            'default_postcode': order.postcode,
            'default_town_or_city': order.town_or_city,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_county': order.county,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    #send email after order
    subject = f'Order Confirmation {order.order_number}'
    message = f'Your order number is {order.order_number}, Thank you for shopping with us!!'
    email_user = [order.email]

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        email_user,
        fail_silently=False,
    )

    
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

def customer_details(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('checkout_success') 
        else:
            context = {
            'customer_form': customer_form,
            }
            return render(request, 'customer_details.html', context)
    else:
        customer_form = CustomerForm()
        context = {
            'customer_form': customer_form,
        }
        return render(request, 'customer_details.html', context)
        

    