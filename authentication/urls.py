from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.user_logout, name="logout"),
    path('<str:username>/', views.details, name="details"),
]
