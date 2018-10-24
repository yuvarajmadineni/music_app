from django.http import HttpResponse
from .models import Album
from django.shortcuts import render
from django.views.generic import ListView

def index(request):
    all_albums = Album.objects.all()
    context = {'album_list' : all_albums }
    return render(request, 'english.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details of the Album id: " + str(album_id) + "</h2>")
