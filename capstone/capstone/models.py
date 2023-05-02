from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, max_length=500)
    image = models.URLField(blank=True, null=True, max_length=500)
    genre = models.CharField(blank=True, null=True, max_length=200)
    platform = models.CharField(blank=True, null=True, max_length=200)
    developer = models.CharField(blank=True, null=True, max_length=200)
    publisher = models.CharField(blank=True, null=True, max_length=200)
    added_by = models.CharField(max_length=64)

    def __str__(self):
        return f"ID# { self.id }: { self.title }"
    
class Playlist(models.Model):
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=64)
    game_id = models.IntegerField()

class Playinglist(models.Model):
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=64)
    game_id = models.IntegerField()
    started_on = models.DateTimeField(auto_now_add=True)

class Playedlist(models.Model):
    title = models.CharField(max_length=200)
    user = models.CharField(max_length=64)
    game_id = models.IntegerField()
    finished_on = models.DateTimeField(auto_now_add=True)