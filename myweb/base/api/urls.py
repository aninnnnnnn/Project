from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_routes),
    path('albums/', views.get_albums),
    path('albums/<str:id>', views.get_album),
]