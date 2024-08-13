from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Album, User, Genre, Artist, Comment, Show, Song
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationFrom, AlbumForm, UserForm, SongForm
from .seeder import seeder_func
from django.contrib import messages


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    seeder_func()
    # albums = Album.objects.all()
    albums = Album.objects.filter(Q(name__icontains=q) | Q(genre__name__icontains=q) | Q(artist__name__icontains=q))
    albums = list(dict.fromkeys(albums))
    genres = Genre.objects.all()
    show = Show.objects.all()
    artists = Artist.objects.all()
    context = {"albums": albums, "genres": genres, "shows": show, "artists": artists}
    return render(request, 'base/home.html', context)


def about(request):
    artists = Artist.objects.all()
    context = {"artists": artists}
    return render(request, 'base/about.html', context)


def shows_page(request):
    show = Show.objects.all()
    artists = Artist.objects.all()
    context = {'shows': show, "artists": artists}
    return render(request, 'base/shows_page.html', context)


@login_required(login_url='login')
def profile(request, pk):
    artists = Artist.objects.all()
    user = User.objects.get(id=int(pk))

    q = request.GET.get('q') if request.GET.get('q') != None else ""

    albums = user.albums.filter(Q(name__icontains=q) | Q(genre__name__icontains=q) | Q(artist__name__icontains=q))
    albums = list(set(albums))
    genres = Genre.objects.all()
    context = {'albums': albums, 'user': user, 'genres': genres, "artists": artists}
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def adding(request, id):
    album = Album.objects.get(id=id)
    user = request.user
    user.albums.add(album)
    return redirect('profile', request.user.id)


def delete(request, id):
    album = Album.objects.get(id=id)
    artists = Artist.objects.all()
    if request.method == "POST":
        request.user.albums.remove(album)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'obj': album, 'artists': artists})


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User or Password is not correct!')

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = MyUserCreationFrom()
    artists = Artist.objects.all()
    if request.method == 'POST':
        form = MyUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'form': form, 'artists': artists}
    return render(request, 'base/register.html', context)


@login_required(login_url='login')
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
                        creator=request.user)

        if not (Album.objects.filter(name=new_album.name)):
            new_album.save()
            new_album.genre.add(genre)
            return redirect('home')

        return redirect('home')

    context = {'form': form, 'artists': artists, 'genres': genres}
    return render(request, 'base/add_album.html', context)


def details(request, id):
    album = Album.objects.get(id=id)
    album_comments = album.comment_set.all().order_by('-created')
    artists = Artist.objects.all()
    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            album=album,
            body=request.POST.get('body')
        )
    return render(request, 'base/details.html', {'album': album, 'comments': album_comments, 'artists': artists})


def delete_album(request, id):
    album = Album.objects.get(id=id)
    artists = Artist.objects.all()
    if request.method == 'POST':
        album.file.delete()
        album.cover.delete()
        album.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': album, 'artists': artists})


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    artists = Artist.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    return render(request, 'base/update_user.html', {'form': form, 'artists':artists})


@login_required(login_url='login')
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    album = comment.album
    artists = Artist.objects.all()
    if request.method == 'POST':
        comment.delete()
        return redirect('details', album.id)
    return render(request, 'base/delete.html', {'obj': comment, 'artists': artists})


@login_required(login_url='login')
def update_album(request, id):
    album = Album.objects.get(id=id)
    form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('details', album.id)

    return render(request, 'base/update_album.html', {'form': form})


def artist_page(request, id):
    artists = Artist.objects.all()
    artist = Artist.objects.get(id=id)
    albums = Album.objects.filter(artist=artist)
    shows = Show.objects.filter(artist=artist)
    return render(request, 'base/artist_page.html', {'artist': artist, 'albums': albums, 'artists': artists, 'shows': shows})