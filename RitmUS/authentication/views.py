from django.shortcuts import render
from base.models import Playlist, Song, User


def home(request):
    playlists =Playlist.objects.all()
    datos = {'playlists': playlists}
    return render(request, 'home.html', datos)

def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    songs = Song.objects.filter(playlist=playlist)
    datos = {'playlist': playlist, 'songs': songs}
    return render(request, 'playlist_details.html', datos)