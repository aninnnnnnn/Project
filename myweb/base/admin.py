from django.contrib import admin
from .models import Album, Artist, User, Genre, Comment, Show, Song
# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Show)
admin.site.register(Song)


