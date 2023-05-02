from django.shortcuts import render

# Create your views here.
def pay_action(requests):
    return render(requests,'payment.html')