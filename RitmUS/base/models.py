from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from enum import Enum

User=get_user_model()

class status(Enum):
    PENDING = 'Pendiente'
    IN_PROGRESS = 'En progreso'
    RESOLVED = 'Resuelta'

class Incidence(models.Model):
    status = models.CharField(max_length=50, choices=[(state.name, state.value) for state in status], default=status.PENDING.name)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
  
class Playlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    genre = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    score = models.FloatField(max_length=5)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist=models.ForeignKey(Playlist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    duration = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    release_date = models.DateTimeField(auto_now_add=True)
    file_url = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.artist

class Order(models.Model):
    purchase_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def total_amount(self):
        total = 0
        for subscription in Subscription.objects.filter(order=self.id).all:
            total += subscription.price
        return total

class Subscription(models.Model):
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    is_favourite = models.BooleanField(default=False)
    
class Cart(models.Model):
    plan = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    