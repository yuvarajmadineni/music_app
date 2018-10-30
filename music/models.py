

from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    albums_logo = models.ImageField(upload_to='',blank=True, null=True)
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length = 250)
    location = models.FileField()

    def __str__(self):
        return self.song_title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song.song_title

class Userdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='',blank=True, null=True)
    lang = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
