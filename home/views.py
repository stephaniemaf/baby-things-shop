from django.shortcuts import render

# Create your views here.

def index (request):
    """ view to return undex page """
    return render(request, "home/index.html")
