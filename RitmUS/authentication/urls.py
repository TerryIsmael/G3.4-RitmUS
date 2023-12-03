from django.urls import path
from .views import home, register,custom_login


urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('user/login/', custom_login, name='custom_login'),
]