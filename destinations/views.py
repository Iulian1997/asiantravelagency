from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger

from .models import Destination

# Create your views here.

def index(request):
    destinations = Destination.objects.all()

    paginator = Paginator(destinations, 1)
    page = request.GET.get('page')
    paged_destinations = paginator.get_page(page)

    context = {
        'destinations': paged_destinations
    }
    return render(request, 'destinations/destinations.html', context)

def destination(request, destination_id):
    return render(request, 'destinations/destination.html')

def search(request):
    return render(request, 'destinations/search.html')
