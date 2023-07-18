from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    number_of_wins = models.IntegerField(default=0)
    number_of_losses = models.IntegerField(default=0)
    team_logo_url = models.TextField(default='')

    def __str__(self):
        return self.name
    

class Player(models.Model):
    photo_url = models.TextField(default='')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    age = models.IntegerField()
    on_injured_reserved_list = models.BooleanField(default=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name