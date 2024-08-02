from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shows/', views.shows, name='shows'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),
    path('add/', views.add_album, name='add'),
    path('details/<str:id>/', views.details, name='details'),
    path('delete_album/<str:id>/', views.delete_album, name='delete_album'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_song/<str:id>/', views.update_song, name='update_song'),
    path('update_album/<str:id>/', views.update_album, name='update_album'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment'),

]
