from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserLoginForm, CreateIncidenceForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.middleware import get_user
from django.contrib.auth.decorators import login_required
from base.models import Incidence

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
    print (incidences[0].status)
    return render(request, 'incidences/listincidence.html', data)