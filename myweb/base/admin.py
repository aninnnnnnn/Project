from django.contrib import admin
from .models import Album, Artist, User, Genre
# Register your models here.
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(User)
admin.site.register(Genre)

