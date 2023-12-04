from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base.models import Order, Subscription, Playlist, Song, User
from datetime import datetime

@login_required
def index(request):
    
    orders = Order.objects.filter(user=request.user.id)
    playlists_owned = []
    
    for order in orders:
        suscriptions = Subscription.objects.filter(order=order.id)
        playlists_owned = [suscription.playlist for suscription in suscriptions if suscription.end_date < datetime.now()]
 
    return render(request, 'index.html', {'playlists': playlists_owned})


'''
def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    songs = Song.objects.filter(playlist=playlist)
    datos = {'playlist': playlist, 'songs': songs}
    return render(request, 'playlist_details.html', datos)
'''