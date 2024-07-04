from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/<str:pk>/', views.profile, name='profile'),
]
