from django.contrib import admin
from .models import Album, Song, Favorite, Userdata

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Favorite)
admin.site.register(Userdata)
