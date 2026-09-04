from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def booking(request):
    return render(request, 'book_table.html')

