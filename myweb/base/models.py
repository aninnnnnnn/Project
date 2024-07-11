from django.db import models
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.SET("Unknown Artist"))
    cover = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, blank=True, related_name='albums')
    file = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.artist} - {self.name}"


class User(AbstractUser):
    albums = models.ManyToManyField(Album, blank=True, related_name='users')

