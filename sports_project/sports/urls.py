from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
    path('teams/', views.TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>', views.TeamList.as_view(), name='team_detail'),
    path('players/', views.PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>', views.PlayerList.as_view(), name='player_detail'),
    path('conference/', views.ConferenceList.as_view(), name='conference_list'),
    path('conference/<int:pk>', views.ConferenceList.as_view(), name='conference_detail'),
]