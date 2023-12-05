from django import forms
from customuser.models import CustomUser as User
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.models import Rating

class CreateRatingForm(forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ['score','description']