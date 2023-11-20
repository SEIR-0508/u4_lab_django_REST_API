# Create your models here.

##Ex.
# tunr/models.py
# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     nationality = models.CharField(max_length=100)
#     photo_url = models.TextField()

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=50)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.location} ({self.division})"

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    injured_reserved = models.BooleanField(default=False)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players') # GPT

    def __str__(self):
        return f"{self.name} - {self.position} ({'IR' if self.injured_reserved else 'Active'})"
