from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Package, Booking

def booking(request):
    if request.method == 'POST':
        ref_code = request.POST['user_id']
        user_id = request.POST['user_id']
        is_ordered = request.POST['is_ordered']
        destination = request.POST['destination']
        destination_id = request.POST['destination_id']
        cost = request.POST['cost']

        booking = Booking(ref_code=ref_code, user_id=user_id, is_ordered=is_ordered, destination=destination, destination_id=destination_id, cost=cost)

        booking.save()
    
        return redirect('accounts/dashboard')