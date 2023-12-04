from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    #path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
]