from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('new_booking', views.new_booking, name="new_booking"),
    path('view_bookings', views.view_bookings, name="view_bookings"),
    path('update_booking/<int:booking_id>', views.update_booking, name="update_booking"),
    path('delete_booking/<int:booking_id>', views.delete_booking, name="delete_booking"),
]
