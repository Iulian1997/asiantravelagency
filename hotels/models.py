from django.db import models
from datetime import datetime
from destinations.models import Destination

class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.name
