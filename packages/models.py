from django.db import models
from datetime import datetime
from destinations.models import Destination
from hotels.models import Hotel


class Package(models.Model):
    destination = models.CharField(max_length=200)
    destination_id = models.IntegerField()
    hotel = models.CharField(max_length=200)
    roomType = models.CharField(max_length=100)
    numberOfGuests = models.CharField(max_length=10)
    breakfast = models.CharField(max_length=100)
    transport = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=50)
    checkIn = models.DateField()
    checkOut = models.DateField()
    visa = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    cost = models.FloatField()
    user_id = models.IntegerField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.destination