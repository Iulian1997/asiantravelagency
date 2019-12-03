from django.db import models
from django.contrib.auth.models import User

from packages.models import Package
from destinations.models import Destination

class Booking(models.Model):
    ref_code = models.CharField(max_length=20)
    user_id = models.IntegerField(blank=True)
    is_ordered = models.BooleanField(default=False)
    destination = models.CharField(max_length=200)
    destination_id = models.IntegerField()
    date_ordered = models.DateTimeField(auto_now=True)
    cost = models.FloatField()
    def __str__(self):
        return self.ref_code

    def get_cost(self):
        x = self.cost / 100 * 15
        return self.cost - x