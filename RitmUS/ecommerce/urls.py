from django.urls import path
from .views import home, playlist_detail, playlist_search



urlpatterns = [
    path('', home, name='home'),
    path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
    path('playlist/search/', playlist_search, name='playlist_search'),
]