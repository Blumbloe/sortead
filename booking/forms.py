from django import forms
from .models import Booking
from . import models
# creating a form 

class CreateBooking (forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ['table','booking_datetime','number_of_guests','status','special_requests']