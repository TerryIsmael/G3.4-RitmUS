from django.urls import path
from .views import home, playlist_detail


urlpatterns = [
    path('', home, name='home'),
      path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
]