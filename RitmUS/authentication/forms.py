from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.models import Incidence

class CreateIncidenceForm(forms.ModelForm):
    
    class Meta:
        model = Incidence
        fields = ['description']

    
        

class CustomUserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

class CustomUserCreationForm(UserCreationForm):

   class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')