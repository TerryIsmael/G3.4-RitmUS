from django.shortcuts import render
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    return render(request, 'registration/register.html', data)
