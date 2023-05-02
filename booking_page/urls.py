from django.contrib import admin
from django.urls import path, include
from . import views
from booking_page.views import bookingaction

app_name="bookingapp"
urlpatterns = [
    path('',bookingaction, name="booking"),
]