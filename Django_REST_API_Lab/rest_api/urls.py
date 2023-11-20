from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('Team/', views.TeamList.as_view(), name='Team_list'),
    path('Team/<int:pk>', views.TeamDetail.as_view(), name='Team_detail'),
    path('Player/', views.PlayerList.as_view(), name="Player_list"),
    path('Player/<int:pk>', views.PlayerDetail.as_view(), name="Player_detail")
]