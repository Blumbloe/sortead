from django import forms
from .models import Booking
from . import models
from .widgets import DateInput
# creating a form 

class CreateBooking (forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = ['table','date','time','number_of_guests','special_requests']

        widgets = {
            'date': DateInput(),
            
        }