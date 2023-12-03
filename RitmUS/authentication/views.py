from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

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
