from django.contrib import admin
from .models import Hotel

class HoteleAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'destination')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'destination')
    list_filter = ('destination',)
    

admin.site.register(Hotel, HoteleAdmin)
