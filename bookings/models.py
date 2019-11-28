from django.db import models
from django.contrib.auth.models import User

from packages.models import Package

class Booking(models.Model):
    ref_code = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(Package)
    date_ordered = models.DateTimeField(auto_now=True)
    cost = models.FloatField()
    def __str__(self):
        return self.ref_code