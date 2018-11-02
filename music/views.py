from django.http import HttpResponse
from django.http import Http404
from .models import Album, Song, Favorite, Userdata
from django.shortcuts import render
from django.views.generic import ListView
from .forms import AlbumForm, SongsForm, FavoriteForm

def english(request):
    all_albums = Album.objects.all()
    context = {'album_list' : all_albums }
    return render(request, 'english.html', context)

def detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        raise Http404("Ablum is not there")
    return render(request, 'song.html', {'album_list' : album })

def telugu(request):
    all_albums = Album.objects.all()
    context = {'album_list' : all_albums }
    return render(request, 'telugu.html', context)

def malayalam(request):
    all_albums = Album.objects.all()
    context = {'album_list' : all_albums }
    return render(request, 'malayalam.html', context)

def favorite(request):
    all_songs = Favorite.objects.filter(user=request.user)
    context = {'favorite' : all_songs }
    return render(request, 'favorite.html', context)

def userinfo(request):
    all_data = Userdata.objects.filter(user=request.user)
    context = { 'user_info' : all_data[0] }
    return render(request, 'home.html', context)

def addnewalbum(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addnewalbum', pk=album.pk)

    else:
        form = AlbumForm()
        return render(request, 'addnewalbum.html' , {'form' : form })

def addnewsong(request):
    if request.method == "POST":
        form = SongsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addnewsong')

    else:
        form = SongsForm()
        return render(request, 'addnewsong.html' , {'form' : form})

def profileuser(request):
    if request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profileuser')

    else:
        form = FavoriteForm()
        return render(request, 'profileuser.html' , {'form' : form})
