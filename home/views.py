from django.utils import timezone
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import Sign_Up, Subscribe_Newsletter
from .models import Customer
from newsletter.models import Subscription, Newsletter

def index(request):
    """ View to return index page """
    return render(request, 'home/index.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
    
def sign_up(request):
    if request.method == 'POST':
        form = Sign_Up(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                customer, created = Customer.objects.get_or_create(user=user)
                return redirect('home')
    else:
        form = Sign_Up()
    return render(request, 'home/sign_up.html', {'form': form})


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = Subscribe_Newsletter(request.POST)
        if form.is_valid():
            email_field = form.cleaned_data['email_field']
            try:
                if Subscription.objects.filter(email_field=email_field).exists():
                    messages.error(request,"This email has already been subscribed to our Newsletter")
                else:
                    subscription = form.save(commit=False)
                    subscription.newsletter = Newsletter.objects.get(title='Welcome To Baby Things')
                    subscription.subscribe_date = timezone.now()
                    subscription.save()
                    messages.success(request, "Thank you for subscribing! Check your inbox for a personal code for money off your first order")  

                    subject = f'Welcome To Baby Things'
                    message = render_to_string('home/welcome_email.txt')
                    email_user = [subscription.email_field]

                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        email_user,
                        fail_silently=False,
                    )
                    return redirect("subscribe_newsletter")
            except Exception as e:
                print (e)
                messages.error(request, "An error has occured while trying to subscribe, Please Try again later.")            
    else:
        form = Subscribe_Newsletter()
    return render(request, 'home/subscribe_newsletter.html', {'form': form})

