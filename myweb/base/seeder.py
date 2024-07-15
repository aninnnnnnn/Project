from .models import Artist, Genre

def seeder_func():
    artists = ['Pink Floyd', "Portishead", "The Doors", "Lebanon Hanover"]
    genres = ['Rock', 'Metal', 'Alternative Rock', 'Classic Rock', 'Post-punk', 'Psychedelic Rock']

    for artist in artists:
        if not Artist.objects.filter(name=artist):
            new_author = Artist(name=artist)
            new_author.save()

    for genre in genres:
        if not Genre.objects.filter(name=genre):
            new_genre = Genre(name=genre)
            new_genre.save()
