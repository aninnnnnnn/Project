from django.shortcuts import render
from django.http import HttpResponse
from .models import Album


def home(request):
    albums = Album.objects.all()
    context = {"albums": albums}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def profile(request):
    return render(request, 'base/profile.html')
