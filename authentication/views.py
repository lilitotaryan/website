from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, get_user
from . import forms


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/authentication/'+str(request.user.username)+'/')
    if request.method == 'POST':
        form = forms.user_login(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username and password):
            raise Http404("Invalid credentials")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            raise Http404("Username or password is not correct!")
        return redirect('/authentication/'+str(username)+'/')
    else:
        form = forms.user_login()
    return render(request, "./authentication/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('/authentication/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/authentication/'+str(request.user.username)+'/')
    if request.method == 'POST':
        form = forms.user_signup(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('username')
        last_name = request.POST.get('password')
        if not(username and password):
            raise Http404("Invalid credentials")
        User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        return redirect('/authentication/')
    else:
        form = forms.user_signup()

    return render(request, "./authentication/signup.html", {"form": form})


def details(request, username):
    if not (request.user.is_authenticated and request.user.username == username):
        raise Http404("No user loged in")
    return render(request, "./authentication/details.html", {"user": request.user})
