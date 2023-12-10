from django import forms
from .models import CustomUser as User
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm, SetPasswordForm
from base.models import Incidence
from django.contrib.auth import authenticate

class CreateIncidenceForm(forms.ModelForm):
    
    class Meta:
        model = Incidence
        fields = ['type','description']

    def __init__(self, *args, **kwargs):
        super(CreateIncidenceForm, self).__init__(*args, **kwargs)
        self.fields['type'].label = "Tipo de incidencia"
        self.fields['type'].choices = self.fields['type'].choices 
        self.fields['description'].label = "Descríbenos el problema"

class CustomUserLoginForm(AuthenticationForm):
    username =  forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'autofocus': True}),label="Correo electrónico")
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'style': 'width: 100%;'}),label="Contraseña")
    error_messages = {
            "invalid_login": (
                "Por favor, introduzca un correo electrónico y una contraseña correctos."
                "Ambos campos pueden ser sensibles a mayúsculas."
            ),
            "inactive": ("Esta cuenta ha sido inhabilitada."),
    }
    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)



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
        super(CustomUserChangePasswordForm, self).__init__(user, *args, **kwargs)
