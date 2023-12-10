from django import forms
from customuser.models import CustomUser as User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.models import Rating

class CreateRatingForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Rating
        fields = ['score','description']
        
    def __init__(self, *args, **kwargs):
            super(CreateRatingForm, self).__init__(*args, **kwargs)
            self.fields['score'].label = "Puntuación"
            self.fields['description'].label = "Descripción" 

class EditRatingForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = Rating
        fields = ['score','description']

        def __init__(self, *args, **kwargs):
            super(EditRatingForm, self).__init__(*args, **kwargs)
            self.fields['score'].label = "Puntuación"
            self.fields['description'].label = "Descripción" 