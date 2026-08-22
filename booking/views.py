from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateBooking
from django.contrib import messages
from .models import Booking
# Create your views here.

def home_view(request):
    context ={}
    form = CreateBooking(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "bookings/book_table.html", context)

@login_required(login_url="/users/login/")
def new_booking(request):
    if request.method == 'POST':
        form = CreateBooking(request.POST, request.FILES)
        if form.is_valid():
            newbooking = form.save(commit=False)
            newbooking.user = request.user
            newbooking.save()
            messages.success(request, "Booking successfully created")
            return redirect('new_booking')
    else:    
        form = CreateBooking()
    return render(request, 'bookings/book_table.html', {'form': form})

@login_required(login_url="/users/login/")
def view_bookings(request):   
    booking = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': booking})

@login_required(login_url="/users/login/")
def update_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = CreateBooking(request.POST, request.FILES, instance=booking)
        if form.is_valid():
            booking.save()
            messages.success(request, "Booking successfully updated")
            return redirect(reverse('view_bookings'))
    else:
        form = CreateBooking(instance=booking)
    return render(request, 'bookings/update_booking.html', {'form': form, 'booking': booking})



@login_required(login_url="/users/login/")
def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        booking.delete()
        return redirect(reverse('view_bookings'))
    return render(request, 'bookings/delete_booking.html')

@login_required(login_url="/users/login/")
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
