from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    TIME_CHOICES = [
        (1, '07:00'),
        (2, '08:00'),
        (3, '09:00'),
        (4, '10:00'),
        (5, '11:00'),
        (6, '12:00'),
        (7, '13:00'),
        (8, '14:00'),
        (9, '15:00'),
        (10, '16:00'),
        (11, '17:00'),
        (12, '18:00'),
        (13, '19:00'),
        (14, '20:00'),
        (15, '21:00'),
        (16, '22:00'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    table = models.OneToOneField(
        'Table', on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True)
    time = models.IntegerField(null=True, choices=TIME_CHOICES)
    number_of_guests = models.PositiveIntegerField(default=1,
                                                   validators=[
                                                       MinValueValidator(1),
                                                       MaxValueValidator(24)])
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.booking_datetime}"


class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Table {self.table_number}"
