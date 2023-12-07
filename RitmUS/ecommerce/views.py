from django.shortcuts import render
from .forms import CreateRatingForm, EditRatingForm
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
    user = request.user
    ratingUser = Rating.objects.filter(playlist=playlist, user=user)
    averageRating = 0
    if ratings.count() > 0:
        for rating in ratings:
            averageRating += rating.score
        averageRating /= ratings.count()
        averageRating = round(averageRating, 2) 
    stars=[2,4,6,8,10]
    users = ratings.count()
    print(users)
    print(averageRating)
    data = {'playlist': playlist, 'songs': songs, 'averageRating': averageRating, "doubleRating": averageRating*2,
             'users': users, 'ratings': ratings, 'stars': stars, 'ratingUser': ratingUser}

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

@login_required
def edit_rating(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    rating = Rating.objects.get(playlist=playlist, user=request.user)
    data = {
        'playlist': playlist,
        'form': EditRatingForm(initial={'user': request.user, 'playlist': playlist, 'score': rating.score, 'description': rating.description})
    }
    if request.method == 'POST':
        form = EditRatingForm(data=request.POST)
        if form.is_valid():
            rating.delete()
            rating = form.save(commit=False)
            rating.user = request.user
            rating.playlist = playlist
            rating.save()
            form.save()
            messages.success(request, 'Reseña editada correctamente')
            return redirect(to='playlist_detail', pk=pk)
        else:
            data['form'] = form

    return render(request, 'ratings/editrating.html', data)

def delete_rating(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    rating = Rating.objects.get(playlist=playlist, user=request.user)
    rating.delete()
    messages.success(request, 'Reseña eliminada correctamente')
    return redirect(to='playlist_detail', pk=pk)

def playlist_search(request):
    query=get_queryset(request)
    data = {'playlists': query}
    return render(request, 'home.html', data)


def get_queryset(request):
        queryset = request.GET.get("search","")
        price_range = request.GET.get('price_range', '')
        queryset2 = Playlist.objects.filter(name__icontains=queryset)
        queryset2 |= Playlist.objects.filter(genre__icontains=queryset)
        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            queryset2 &= Playlist.objects.filter(price__gte=min_price, price__lte=max_price)
        return queryset2





