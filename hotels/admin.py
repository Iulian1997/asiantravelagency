from django.contrib import admin
from .models import Hotel

class HoteleAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name',)
    list_display_links = ('id', 'name')
    

admin.site.register(Hotel, HoteleAdmin)
