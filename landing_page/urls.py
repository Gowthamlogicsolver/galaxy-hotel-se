from django.contrib import admin
from django.urls import path, include
from . import views
from landing_page.views import landingaction

app_name="landingapp"
urlpatterns = [
    path('',landingaction, name="landing"),
]