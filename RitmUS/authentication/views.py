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

def playlist_search(request):
    query=get_queryset(request)
    datos = {'playlists': query}
    return render(request, 'home.html', datos)


def get_queryset(request):
        queryset = request.GET.get("search","")
        price_range = request.GET.get('price_range', '')
        print(queryset)
        queryset2 = Playlist.objects.filter(name__icontains=queryset)
        queryset2 |= Playlist.objects.filter(genre__icontains=queryset)
        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            queryset2 &= Playlist.objects.filter(price__gte=min_price, price__lte=max_price)
        return queryset2