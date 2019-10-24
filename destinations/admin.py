from django.contrib import admin

from .models import Destination

# Display other fields in destinations admin page
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'city', 'cost', 'is_published')
    list_display_links = ('id', 'name') # Click on name to load destination
    list_filter = ('country',)
    list_editable = ('is_published',)
    search_fields = ('country', 'description', 'city')
    list_per_page = 25

admin.site.register(Destination, DestinationAdmin)

