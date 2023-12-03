from django.shortcuts import render
from base.models import Playlist, Song, User


def home(request):
    playlists =Playlist.objects.all()
    datos = {'playlists': playlists}
    return render(request, 'home.html', datos)
