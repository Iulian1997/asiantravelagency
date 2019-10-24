from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='destinations'),
    path('<int:destination_id>', views.destination, name='destination'),
    path('search', views.search, name='search'),
]