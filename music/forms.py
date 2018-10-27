from django import forms

from .models import Album, Song

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'title','genre','albums_logo','language']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = [ 'album', 'file_type', 'song_title' , 'is_liked']
