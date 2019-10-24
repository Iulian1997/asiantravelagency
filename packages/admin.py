from django.contrib import admin

from .models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display = ('id' ,'destination', 'name', 'address', 'email', 'number')
    list_display_links = ('id', 'destination')
    

admin.site.register(Package, PackageAdmin)
