from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'destinations/destinations.html')

def destination(request):
    return render(request, 'destinations/destination.html')

def search(request):
    return render(request, 'destinations/search.html')
