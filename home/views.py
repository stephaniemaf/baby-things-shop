from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Sign_Up, Subscribe_Newsletter
from .models import Customer
from newsletter.models import Subscription, Newsletter
from datetime import datetime

def index(request):
    """ View to return index page """
    return render(request, 'home/index.html')

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
                    subscription.newsletter = Newsletter.objects.get(title='Welcome to Baby Things')
                    subscription.subscribe_date = datetime.now()
                    subscription.save()
                    messages.success(request, "Thank you for subscribing!")   
                    return redirect("subscribe_newsletter")
            except Exception as e:
                error = messages.error(request, f"There has been an error: {str(e)}. Please try again later.")   
                print(error)       
    else:
        form = Subscribe_Newsletter()
    return render(request, 'home/subscribe_newsletter.html', {'form': form})