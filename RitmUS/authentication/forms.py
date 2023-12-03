from django import forms
#from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    pass
   # class Meta:
    #    model = User
     #   fields = ('username', 'email', 'first_name', 'last_name')