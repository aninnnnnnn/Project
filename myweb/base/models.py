from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=200)
    cover = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.artist} - {self.name}"