from django.contrib import admin
from .models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'destination', 'hotel', 'roomType', 'breakfast', 'transport', 'numberOfGuests', 'checkIn', 'checkOut', 'cost')
    list_display_links = ('id' ,'name', 'destination')
    

admin.site.register(Package, PackageAdmin)
