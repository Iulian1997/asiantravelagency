from django.shortcuts import render
from django.http import HttpResponse
from destinations.choices import country_choices, price_choices

from destinations.models import Destination

def index(request):
    destinations = Destination.objects.order_by('-list_date').filter(is_published=True)[:3] # Show only 3 destinations

    context = {
        'destinations': destinations,
        'country_choices': country_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

