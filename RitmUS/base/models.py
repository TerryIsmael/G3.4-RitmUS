from django.db import models
from django.contrib.auth import get_user_model
from enum import Enum
import datetime
from datetime import timedelta

User=get_user_model()

class Status(Enum):
    PENDING = 'Pendiente'
    IN_PROGRESS = 'En progreso'
    RESOLVED = 'Resuelta'

class Type(Enum):
    BUG = 'Error'
    FEATURE = 'Funcionalidad'
    DEL_ACCOUNT = 'Borrar cuenta'
    OTHER = 'Otros'

class Incidence(models.Model):
    status = models.CharField(max_length=50, choices=[(state.name, state.value) for state in Status], default=Status.PENDING.name)
    description = models.TextField(max_length=500)
    date = models.DateTimeField(default = datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=[(t.name, t.value) for t in Type], default=Type.OTHER.name)
    
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
    date = models.DateTimeField(default = datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist=models.ForeignKey(Playlist, on_delete=models.CASCADE)

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    duration = models.IntegerField()
    image = models.ImageField(upload_to='static/img/')
    release_date = models.DateTimeField(default = datetime.datetime.now())
    file_url = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.artist

class Order(models.Model):
    purchase_date = models.DateTimeField(default = datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def total_amount(self):
        total = 0
        for subscription in Subscription.objects.filter(order=self.id).all():
            total += subscription.price
        return total

class Subscription(models.Model):
    init_date = models.DateTimeField(default = datetime.datetime.now())
    end_date = models.DateTimeField(default = datetime.datetime.now() + timedelta(days=30))
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    is_favourite = models.BooleanField(default=False)
    
class Cart(models.Model):
    plan = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Playlist)
    