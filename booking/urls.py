from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('new_booking', views.new_booking, name="new booking"),
]
