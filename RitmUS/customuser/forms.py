from django import forms
from .models import CustomUser as User
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.models import Incidence

class CreateIncidenceForm(forms.ModelForm):
    
    class Meta:
        model = Incidence
        fields = ['description']

    
class CustomUserLoginForm(AuthenticationForm):
    

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'] = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
        self.fields['username'].label = "Correo electrónico"

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')