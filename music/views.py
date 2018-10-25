from django.http import HttpResponse
from django.http import Http404
from .models import Album
from django.shortcuts import render
from django.views.generic import ListView

def index(request):
    all_albums = Album.objects.all()
    context = {'album_list' : all_albums }
    return render(request, 'english.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Ablum is not there")
    return render(request, 'song.html', {'album_list' : album })
