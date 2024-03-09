from django.shortcuts import render, redirect
from .forms import Sign_Up

def index(request):
    """ view to return undex page """
    
    return render(request, 'home/index.html')

def sign_up(request):
    if request.method == 'POST':
        form = Sign_Up(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return redirect('home') 
    else:
        form = Sign_Up()
    return render(request, 'home/sign_up.html', {'form': form})



