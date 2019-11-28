from django.contrib import admin
from .models import Booking, Package

class BookingAdmin(admin.ModelAdmin):
    list_display =('ref_code', 'owner', 'is_ordered', 'date_ordered', 'cost')

admin.site.register(Booking, BookingAdmin)