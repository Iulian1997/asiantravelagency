from django.urls import path

from . import views 

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('order-summary', views.order_summary, name='order_summary'),
    path('checkout', views.checkout, name='checkout'),
]