

from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    albums_logo = models.CharField(max_length=1000)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length = 250)
    is_liked = models.BooleanField(default = False)
    location = models.FileField()

    def __str__(self):
        return self.song_title
