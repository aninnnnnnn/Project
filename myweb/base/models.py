from django.db import models
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=200)
    showdate = models.DateTimeField(null=True, blank=True)
    show = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown Creator"))
    artist = models.ForeignKey(Artist, on_delete=models.SET("Unknown Artist"))
    cover = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, blank=True, related_name='albums')


    created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.artist} - {self.name}"


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    audio_file = models.FileField(null=True, blank=True, upload_to='songs/')
    duration = models.DurationField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    albums = models.ManyToManyField(Album, blank=True, related_name='users')
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.jpg')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body

