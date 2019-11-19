from django.db import models
from datetime import datetime

class Booking(models.Model):
    destination = models.CharField(max_length=200)
    destination_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    booking_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
