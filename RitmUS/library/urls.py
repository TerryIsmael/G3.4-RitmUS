from django.urls import path
from .views import index, playlist_detail

urlpatterns = [
    path('/galeria', index, name='index'),
    #path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
]