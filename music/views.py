from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
from django.views.generic import ListView

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums }
    return render(request, 'music/english.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details of the Album id: " + str(album_id) + "</h2>")

class EnglishAlbumView(ListView):
    model = Album.objects.all()
    template_name = "english.html"
