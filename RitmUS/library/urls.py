from django.urls import path
from .views import index, library_playlist_detail, toggle_favourite, library_playlist_search

urlpatterns = [
    path('', index, name='index'),
    path('playlist/<int:pk>/', library_playlist_detail, name='library_playlist_detail'),
    path('subscription/toggle_favourite/<int:id>/', toggle_favourite, name='toggle_favourite'),
    path('playlist/search/', library_playlist_search, name='library_playlist_search')
]