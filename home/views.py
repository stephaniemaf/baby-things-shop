from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Sign_Up, Subscribe_Newsletter
from .models import Customer
from newsletter.models import Subscription

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
            try:
                form.save()
                email = form.cleaned_data['email']
                messages.success(request,'You have successfully subscribed to our newsletter')
            except Exception as e:
                messages.error(request,'There was an Error when subscribing. Please try again later')
        else:
            messages.error(request, 'Invalid email, Please enter your email again')
        return redirect('subscribe_newsletter')      
    else:
        form = Subscribe_Newsletter()
    
    return render(request, 'home/subscribe_newsletter.html', {'form': form})

