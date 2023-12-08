from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('playlist/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('playlist/search/', views.playlist_search, name='playlist_search'),
    path('create_rating/<int:pk>/', views.create_rating, name='create_rating'),
    path('edit_rating/<int:pk>/', views.edit_rating, name='edit_rating'),
    path('delete_rating/<int:pk>/', views.delete_rating, name='delete_rating'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/completed', views.checkout_completed, name='checkout_completed'),

]