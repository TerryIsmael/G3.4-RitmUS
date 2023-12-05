from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserLoginForm, CreateIncidenceForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from base.models import Playlist, Song, User, Incidence

def home(request):
    return render(request, 'home.html')



def custom_login(request):
    data = {
        'form': CustomUserLoginForm()
    }
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            form.save()
            userAux = User.objects.filter(email=form.cleaned_data['email']).first()
            print(userAux)
            user = authenticate(
                username= userAux.username,
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, 'Logueado')
            return redirect(to='home')
        else:
            data['form'] = form
    return render(request, 'registration/login.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(request, 'Registrado correctamente')
            return redirect(to='home')
        else:
            data['form'] = form
    return render(request, 'registration/register.html', data)

@login_required
def create_incidence(request):
    data = {
        'form': CreateIncidenceForm(initial={'user': request.user})
    }
    if request.method == 'POST':
        form = CreateIncidenceForm(data=request.POST)
        if form.is_valid():
            incidence = form.save(commit=False)
            incidence.user = request.user
            incidence.save()
            form.save()
            messages.success(request, 'Incidencia creada correctamente')
            data['message'] = 'Incidencia creada correctamente'
            return redirect(to='list_incidences')
        else:
            data['form'] = form

    return render(request, 'incidences/newincidence.html', data)

def list_incidences(request):
    incidences = Incidence.objects.filter(user=request.user) 
    data = {
        'incidences': incidences
    }
    return render(request, 'incidences/listincidence.html', data)

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