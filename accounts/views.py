from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail

from packages.models import Package
from bookings.models import Booking



def register(request):
    if request.method == 'POST':
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validating password
        if password == password2:
            # Checking username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken.')
                return redirect('register')
            else:
                # Checking email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used.')
                    return redirect('register')
                else:
                    # Registering User
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('order_summary')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')


def order_summary(request):
    user_package = Package.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'packages': user_package
    }

    return render(request, 'cart/order_summary.html', context)


def checkout(request):
    booking = Package.objects.order_by(
        '-contact_date').filter(user_id=request.user.id)

    context = {
        'bookings': booking
    }

    return render(request, 'cart/checkout.html', context)


def dashboard(request):
    bookings = Booking.objects.all()

    context = {
        'bookings': bookings
    }
    return render(request, 'accounts/dashboard.html', context)


def delete_from_cart(request, destination_id):
    order_item = Package.objects.filter(destination_id=destination_id)

    order_item.delete()

    context = {
        'order_item': order_item
    }

    return redirect(order_summary)

def cancel_holiday(request, ref_code, destination):
    holiday = Booking.objects.filter(ref_code=ref_code)

    send_mail(
            'Holiday Cancellation Reference Number '+str(ref_code),
            'You have cancelled your holiday to ' + destination,
            'xJJx97x@gmail.com',
            ['Iulian.Gherman@mycit.ie'],
            fail_silently=False
        )

    holiday.delete()

    context = {
        'holiday': holiday
    }

    

    messages.success(request, 'Holiday has now been cancelled.')


    return redirect(dashboard)