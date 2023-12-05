from django.urls import path
from .views import home, playlist_detail, playlist_search, create_rating



urlpatterns = [
    path('', home, name='home'),
    path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
    path('playlist/search/', playlist_search, name='playlist_search'),
    path('create_rating/<int:pk>/', create_rating, name='create_rating')
]