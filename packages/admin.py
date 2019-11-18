from django.contrib import admin
from .models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display = ('id' ,'destination', 'hotel', 'roomType', 'breakfast', 'transport', 'numOfGuests', 'checkInDate', 'checkOutDate')
    list_display_links = ('id', 'destination')
    

admin.site.register(Package, PackageAdmin)
