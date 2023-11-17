from django.shortcuts import render
from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer, ConferenceSerializer
from .models import Team, Player, Conference

# Create your views here.

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

class ConferenceList(generics.ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer


class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer