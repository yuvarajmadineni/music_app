from django import forms

from .models import Album, Song, Favorite, Userdata

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'title','genre','albums_logo','language']


class SongsForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = [ 'album', 'file_type', 'song_title' , 'location']

class FavoriteForm(forms.ModelForm):

    class Meta:
        model = Favorite
        fields = [ 'user', 'song' ]

class UserForm(forms.ModelForm):

    class Meta:
        model = Userdata
        fields = [ 'user', 'user_picture', 'lang' ]
