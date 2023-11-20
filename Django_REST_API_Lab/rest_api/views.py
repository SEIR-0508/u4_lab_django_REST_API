from django.shortcuts import render

# Create your views here.
# views.py
# from django.http import JsonResponse

# def team_list(request):
#     teams = teams.objects.all().values('name', 'location', 'division', 'wins', 'losses') # only grab some attributes from our database, else we can't serialize it.
#     team_list = list(Teams) # convert our Teams to a list instead of QuerySet
#     return JsonResponse(team_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

# views.py

from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer
from .models import Team, Player

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer