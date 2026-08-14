from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateBooking
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
        form = forms.CreateBooking(request.POST, request.FILES)
        if form.is_valid():
            newbooking = form.save(commit=False)
            newbooking.user = request.user
            newbooking.save()
            return redirect('book_table')
    else:    
        form = forms.CreatePost()
    return render(request, 'bookings/book_table.html', {'form': form})




