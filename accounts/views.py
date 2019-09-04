from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login, get_user


def profile(request):
    return render(request, "./accounts/profile.html")

def logged_out(user):
    return user.is_anonymous

# @user_passes_test(logged_out)
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
            if user is not None:
                login(user)
                return redirect( "accounts/profile/")
            return HttpResponse('Unauthorized', status=401)
        return HttpResponse('Forbidden', status=403)
    else:
        form = AuthenticationForm()
    return render(request, "./accounts/login.html", {"form": form})


@login_required(login_url='/accounts/login/')
def logout(request):
    logout(request)
    return redirect('/authentication/')


@user_passes_test(logged_out)
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            User.objects.create_user(username=username, password=password1)
            return redirect(login)
        return HttpResponse('Bad Request', status=400)
    else:
        form = UserCreationForm()

    return render(request, "./accounts/signup.html", {"form": form})


@login_required(login_url='/accounts/login/')
def details(request, username):
    if not (request.user.is_authenticated and request.user.username == username):
        raise Http404("No user loged in")
    return render(request, "./authentication/details.html", {"user": request.user})
