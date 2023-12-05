from django.contrib import admin
from .models import Incidence, Playlist, Rating, Song, Order, Subscription, Cart

# Register your models here.
admin.site.register(Incidence)
admin.site.register(Playlist)
admin.site.register(Rating)
admin.site.register(Song)
admin.site.register(Order)
admin.site.register(Subscription)
admin.site.register(Cart)



