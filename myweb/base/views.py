from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, User


def home(request):
    albums = Album.objects.all()
    context = {"albums": albums}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def profile(request, pk):
    user = User.objects.get(id=int(pk))
    albums = user.albums.all()
    context = {'albums': albums, 'user': user}
    return render(request, 'base/profile.html', context)


