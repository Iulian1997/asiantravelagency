from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('destinations/', include('destinations.urls')),
    path('admin/', admin.site.urls),
]
