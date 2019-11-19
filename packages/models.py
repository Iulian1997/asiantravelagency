from django.db import models
from datetime import datetime
from destinations.models import Destination
from hotels.models import Hotel


class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.DO_NOTHING, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING, null=True)
    roomType = models.CharField(max_length=100)
    breakfast = models.BooleanField(default=True)
    transport = models.BooleanField(default=True)
    numOfGuests = models.IntegerField()
    checkInDate = models.DateTimeField()
    checkOutDate = models.DateTimeField()
    visa = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.destination.name