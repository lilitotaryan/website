from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Order


def orders(username, request):
    User.objects.all(username=username, )
    return render(request, "./orders/index.html", {})

def details(username, request):
    pass
