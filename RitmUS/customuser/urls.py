from django.urls import path
from .views import home, register,custom_login, create_incidence, list_incidences, playlist_detail, playlist_search



urlpatterns = [
    path('register/', register, name='register'),
    path('user/login/', custom_login, name='custom_login'),
    path('incidence/new/', create_incidence, name='create_incidence'),
    path('incidence/list/', list_incidences, name='list_incidences'),
    path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
    path('playlist/search/', playlist_search, name='playlist_search'),
]