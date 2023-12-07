from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from base.models import Order, Subscription, Playlist, Song
from datetime import datetime, timezone, timedelta
import locale

@login_required
def index(request):

    orders = Order.objects.filter(user=request.user.id)
    active_subs = []
    
    for order in orders:
        subscriptions = Subscription.objects.filter(order=order)
        active_subs = active_subs + [subscription for subscription in subscriptions if subscription.end_date > datetime.now(timezone.utc)]

    return render(request, 'index.html', {'subscriptions': active_subs})

@login_required
def library_playlist_detail(request, pk):

    playlist = Playlist.objects.get(pk=pk)
    subscription = Subscription.objects.filter(playlist=playlist, order__user= request.user, end_date__gt=datetime.now(timezone.utc)).first()
    songs = Song.objects.filter(playlist=playlist)

    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    correct_date = subscription.end_date + timedelta(hours=1)
    formatted_date = correct_date.strftime("%d/%m/%Y %H:%M")

    return render(request, 'library_playlist_details.html', {'subscription': subscription, 'songs': songs, 'subscription_end_date': formatted_date})

@login_required
def toggle_favourite(request, id):

    subscription = Subscription.objects.get(pk=id)
    subscription.is_favourite = not subscription.is_favourite
    subscription.save()        
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def library_playlist_search(request):

    query=get_queryset(request)
    queryset = request.GET.get("search","")
    queryfav = request.GET.get("search_favourite","")

    return render(request, 'index.html', {'subscriptions': query, 'queryset': queryset, 'queryfav': queryfav})

@login_required
def get_queryset(request):

    orders = Order.objects.filter(user=request.user.id)
    active_subs = []
    
    for order in orders:
        subscriptions = Subscription.objects.filter(order=order)
        active_subs = active_subs + [subscription for subscription in subscriptions if subscription.end_date > datetime.now(timezone.utc)]

    queryset = request.GET.get("search","")
    queryfav = request.GET.get("search_favourite","")
    queryset2 = Playlist.objects.filter(name__icontains=queryset)
    queryset2 |= Playlist.objects.filter(genre__icontains=queryset)

    if queryfav == "on":
        res = [subscription for subscription in active_subs if subscription.playlist in queryset2 and subscription.is_favourite]
    else:
        res = [subscription for subscription in active_subs if subscription.playlist in queryset2]
    
    return res
