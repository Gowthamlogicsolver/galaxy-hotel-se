from django.contrib import admin
from django.urls import path, include
from . import views
from login_page.views import login_action,logout_action

app_name="loginapp"
urlpatterns = [
    path('',login_action, name="login"),
    path('logout/',logout_action, name="logout"),
    
]