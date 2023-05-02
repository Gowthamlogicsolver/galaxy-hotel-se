from django.contrib import admin
from django.urls import path, include
from . import views
from payment_page.views import pay_action

app_name="paymentapp"
urlpatterns = [
    path('',pay_action, name="pay"),
    
]