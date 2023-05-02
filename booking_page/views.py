from django.shortcuts import render

# Create your views here.
def bookingaction(requests):
    return render(requests,'booking.html')
