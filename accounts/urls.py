from django.urls import path

from . import views 

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('order-summary', views.order_summary, name='order_summary'),
    path('updated-cart<int:destination_id>', views.delete_from_cart, name='delete_from_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('dashboard', views.dashboard, name='dashboard')
]