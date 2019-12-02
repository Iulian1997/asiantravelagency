from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Package, Hotel

def package(request):
    if request.method == 'POST':
        destination = request.POST['destination']
        destination_id = request.POST['destination_id']
        hotel = request.POST['hotel']
        roomType = request.POST['roomType']
        numberOfGuests = request.POST['numberOfGuests']
        breakfast = request.POST['breakfast']
        transport = request.POST['transport']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        checkIn = request.POST['checkIn']
        checkOut = request.POST['checkOut']
        visa = request.POST['visa']
        passport = request.POST['passport']
        cost = request.POST['cost']
        user_id = request.POST['user_id']

        # Check if user is logged in
        if request.user.is_authenticated:

            # If there are no hotels
            if hotel != 'No Hotels':

                package = Package(destination=destination, destination_id=destination_id, hotel=hotel, roomType=roomType, numberOfGuests=numberOfGuests, breakfast=breakfast, transport=transport, name=name, email=email, mobile=mobile, checkIn=checkIn, checkOut=checkOut, visa=visa, passport=passport, cost=cost, user_id=user_id)

                package.save()

                # Send email
                send_mail(
                    'Holiday Booking Confirmation',
                    'You have booked a holiday to ' +destination +'.',
                    'xJJx97x@gmail.com',
                    ['Iulian.Gherman@mycit.ie'],
                    fail_silently=False
                )

                messages.success(request, 'Your package has been added to cart.')
                return redirect('/destinations/'+destination_id)

            else:
                messages.error(request, 'Sorry no hotels available for this destination.')
                return redirect('/destinations/'+destination_id)

        else:
            messages.error(request, 'Please login to book your holiday.')
            return redirect('/destinations/'+destination_id)
        
