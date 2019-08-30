from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from . import forms

def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not (username and password):
        raise Http404("Invalid credentials")
    user = authenticate(request, username=username, password=request.password)
    login(request, user)
    return render(request, "./authenticate/login.html")


def user_logout(request):
    logout(request)
    return render(request, "./authenticate/logout.html")


def signup(request):
    print(request.method)
    if request.method == 'POST':
        print(request.method)
        form = forms.signup(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('username')
        last_name = request.POST.get('password')
        if not(username and password):
            raise Http404("Invalid credentials")
        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        return redirect('/authentication/')
    else:
        form = forms.signup()

    return render(request, "./authenticate/signup.html", {"form":form})

