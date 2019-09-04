from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name="orders"),
    path('details/', views.details, name="details"),
]
