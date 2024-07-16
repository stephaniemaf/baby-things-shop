from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Sign_Up, Subscribe_Newsletter
from .models import Customer
from newsletter.models import Subscription, Newsletter

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
            email = form.cleaned_data['email']
            try:
                subscription = form.save(commit=False)
                subscription.newsletter = Newsletter.objects.get(title='Welcome to Baby Things')
                subscription.save()
                messages.success(request, "Thank you for subscribing!")   
                return redirect("subscribe_newsletter")
            except Exception as e:
                messages.error(request, "There as been an error please try again later")          
    else:
        form = Subscribe_Newsletter()
    return render(request, 'home/subscribe_newsletter.html', {'form': form})