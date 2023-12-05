from django.urls import path
from .views import index, library_playlist_detail

urlpatterns = [
    path('', index, name='index'),
    path('playlist/<int:pk>/', library_playlist_detail, name='library_playlist_detail'),
]