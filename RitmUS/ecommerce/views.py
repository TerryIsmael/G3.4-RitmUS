from django.shortcuts import render
from .forms import CreateRatingForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import Playlist,User, Song, Rating
from django.contrib import messages

def home(request):
    playlists = Playlist.objects.all()
    data = {'playlists': playlists}
    return render(request, 'home.html', data)


def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    songs = Song.objects.filter(playlist=playlist)
    ratings = Rating.objects.filter(playlist=playlist)
    averageRating = 0
    if ratings.count() > 0:
        for rating in ratings:
            averageRating += rating.score
        averageRating /= ratings.count()
        averageRating = round(averageRating, 2) 
    stars=[0,1,2,3,4]
    users = ratings.count()
    print(users)
    print(averageRating)
    data = {'playlist': playlist, 'songs': songs, 'averageRating': averageRating, 'users': users, 'ratings': ratings, 'stars': stars}

    return render(request, 'playlist_details.html', data)

@login_required
def create_rating(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    data = {
        'playlist': playlist,
        'form': CreateRatingForm(initial={'user': request.user, 'playlist': playlist})
    }
    if request.method == 'POST':
        form = CreateRatingForm(data=request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.playlist = playlist
            rating.save()
            form.save()
            messages.success(request, 'Reseña creada correctamente')
            return redirect(to='playlist_detail', pk=pk)
        else:
            data['form'] = form

    return render(request, 'ratings/createrating.html', data)

def playlist_search(request):
    query=get_queryset(request)
    data = {'playlists': query}
    return render(request, 'home.html', data)


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





