from django.urls import path
from .views import home, playlist_detail, playlist_search, create_rating, edit_rating, delete_rating, add_to_cart



urlpatterns = [
    path('', home, name='home'),
    path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
    path('playlist/search/', playlist_search, name='playlist_search'),
    path('create_rating/<int:pk>/', create_rating, name='create_rating'),
    path('edit_rating/<int:pk>/', edit_rating, name='edit_rating'),
    path('delete_rating/<int:pk>/', delete_rating, name='delete_rating'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
]