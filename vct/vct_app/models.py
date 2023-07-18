from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, default='')
    nationality = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = 'players', default='')

    def __str__(self):
        return self.name
    
