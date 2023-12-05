from django.urls import path
from .views import register,custom_login, create_incidence, list_incidences



urlpatterns = [
    path('register/', register, name='register'),
    path('user/login/', custom_login, name='custom_login'),
    path('incidence/new/', create_incidence, name='create_incidence'),
    path('incidence/list/', list_incidences, name='list_incidences'),
  
]