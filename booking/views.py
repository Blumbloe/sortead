from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateBooking
from django.contrib import messages
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
            return redirect('bookings/book_table.html')
    else:    
        form = CreateBooking()
    return render(request, 'bookings/book_table.html', {'form': form})

