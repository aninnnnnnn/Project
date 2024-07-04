from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, User, Genre
from django.db.models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    # albums = Album.objects.all()
    albums = Album.objects.filter(Q(name__icontains=q) | Q(genre__name__icontains=q) | Q(artist__name__icontains=q))
    albums = list(set(albums))
    genres = Genre.objects.all()
    context = {"albums": albums, "genres": genres}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def profile(request, pk):
    user = User.objects.get(id=int(pk))

    q = request.GET.get('q') if request.GET.get('q') != None else ""

    albums = user.albums.filter(Q(name__icontains=q) | Q(genre__name__icontains=q) | Q(artist__name__icontains=q))
    albums = list(set(albums))
    genres = Genre.objects.all()
    context = {'albums': albums, 'user': user, 'genres': genres}
    return render(request, 'base/profile.html', context)


