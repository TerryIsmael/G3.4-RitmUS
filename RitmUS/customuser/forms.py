from django import forms
from .models import CustomUser as User
#from django.contrib.auth.models import User
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm, SetPasswordForm
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

class CustomUserCreationForm(BaseUserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'custom-password-input'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'custom-password-input'})

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name') 

class CustomUserChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        user = request.user

        # Pass the actual user object to SetPasswordForm
        super(CustomUserChangePasswordForm, self).__init__(user, *args, **kwargs)