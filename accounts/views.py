from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


@login_required(login_url='log_in')
def details(request):
    return render(request, "./accounts/details.html", {"user": request.user})


def logged_out(user):
    return user.is_anonymous


@user_passes_test(logged_out, login_url='details')
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("username"),
                                password=form.cleaned_data.get("password"))
            if user is not None:
                login(request, user)
                return redirect('details')
            return HttpResponse('Unauthorized', status=401)
        return HttpResponse('Forbidden', status=403)
    else:
        form = AuthenticationForm()
    return render(request, "./accounts/login.html", {"form": form})


@login_required(login_url='log_in')
def log_out(request):
    logout(request)
    return redirect('log_in')


@user_passes_test(logged_out, login_url='details')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            User.objects.create_user(username=username, password=password1)
            return redirect('log_in')
        return HttpResponse('Bad Request', status=400)
    else:
        form = UserCreationForm()

    return render(request, "./accounts/signup.html", {"form": form})