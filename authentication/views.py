from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout


# Create your views here.
def user_login(request):
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    return render(request, "./authenticate/index.html", {"username": user.username})


def user_logout(request):
    logout(request)


def signup(request):
    User.objects.create_user(request, username=request.POST["username"], password=request.POST["password"], first_name=request.POST["name"], last_name=request.POST["name"])
