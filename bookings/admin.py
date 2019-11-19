from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name')
    list_display_links = ('id', 'name')
    

admin.site.register(Booking, BookingAdmin)
