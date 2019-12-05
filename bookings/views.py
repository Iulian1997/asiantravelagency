from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Package, Booking
from bookings.extras import generate_ref_id


def booking(request):
    if request.method == 'POST':
        ref_code = generate_ref_id()
        user_id = request.POST['user_id']
        user_email = request.POST['user_email']
        is_ordered = request.POST['is_ordered']
        destination = request.POST['destination']
        destination_id = request.POST['destination_id']
        checkIn = request.POST['checkIn']
        checkOut = request.POST['checkOut']
        cost = request.POST['cost']

        booking = Booking(ref_code=ref_code, user_id=user_id, user_email=user_email, is_ordered=is_ordered, destination=destination, destination_id=destination_id, checkIn=checkIn, checkOut=checkOut, cost=cost)

        booking.save()

        # Send email
        send_mail(
            'Holiday Booking Confirmation',
            'You have booked a holiday to ' + destination + '.\n'
            '\nYour reference number is ' + ref_code +', visit your dashboard to see more details.\n'
            '\nTotal cost: €' +cost,
            'xJJx97x@gmail.com',
            [user_email],
            fail_silently=False
        )

        return redirect('accounts/dashboard')
