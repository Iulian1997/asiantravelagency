from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from .choices import country_choices, price_choices

from .models import Destination

# Create your views here.

def index(request):
    destinations = Destination.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(destinations, 6)
    page = request.GET.get('page')
    paged_destinations = paginator.get_page(page)

    context = {
        'destinations': paged_destinations
    }
    return render(request, 'destinations/destinations.html', context)

def destination(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)

    context = {
        'destination': destination
    }

    return render(request, 'destinations/destination.html', context)

def search(request):
    queryset_list = Destination.objects.order_by('-list_date')

    # Search by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Search by city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Search by price
    if 'cost' in request.GET:
        cost = request.GET['cost']
        if cost:
            queryset_list = queryset_list.filter(cost__lte=cost)

    context = {
        'country_choices': country_choices,
        'price_choices': price_choices,
        'destinations': queryset_list,
        'values': request.GET
    }

    return render(request, 'destinations/search.html', context)
