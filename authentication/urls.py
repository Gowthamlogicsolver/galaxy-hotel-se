from django.contrib import admin
from django.urls import path, include
from . import views
from authentication.views import signaction

app_name="signupapp"
urlpatterns = [
    path('',signaction, name="signup"),
]