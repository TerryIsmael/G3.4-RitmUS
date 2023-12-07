from django import forms
from customuser.models import CustomUser as User
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.models import Rating

class CreateRatingForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Rating
        fields = ['score','description']

class EditRatingForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Rating
        fields = ['score','description']