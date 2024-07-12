from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, User, Genre, Artist
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationFrom, AlbumForm


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    # albums = Album.objects.all()
    albums = Album.objects.filter(Q(name__icontains=q) | Q(genre__name__icontains=q) | Q(artist__name__icontains=q))
    albums = list(set(albums))
    genres = Genre.objects.all()
    context = {"albums": albums, "genres": genres}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
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


def adding(request, id):
    album = Album.objects.get(id=id)
    user = request.user
    user.albums.add(album)
    return redirect('home')


def delete(request, id):
    album = Album.objects.get(id=id)
    if request.method == "POST":
        request.user.albums.remove(album)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'album': album})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            pass  # error message

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass  # error

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = MyUserCreationFrom()

    if request.method == 'POST':
        form = MyUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/register.html', context)


def add_album(request):
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    form = AlbumForm()

    if request.method == 'POST':
        album_artist = request.POST.get('artist')
        album_genre = request.POST.get('genre')

        artist, created = Artist.objects.get_or_create(name=album_artist)
        genre, created = Genre.objects.get_or_create(name=album_genre)

        form = AlbumForm(request.POST)
        new_album = Album(cover=request.FILES['cover'], name=form.data['name'], artist=artist, year=form.data['year'],
                          file=request.FILES['file'])

        new_album.save()
        new_album.genre.add(genre)

        return redirect('home')

    context = {'form': form, 'artists': artists, 'genres': genres}
    return render(request, 'base/add_album.html', context)