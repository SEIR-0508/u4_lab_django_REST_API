from rest_framework import serializers
from .models import Team, Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name = 'team_detail',
        read_only = True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset = Team.objects.all(),
        source = 'team'
    )
    player = serializers.HyperlinkedRelatedField(
        view_name = 'player_detail',
        read_only = True
    )
    
    class Meta:
        model = Player
        fields = ('id', 'nickname', 'name', 'age', 'nationality', 'team', 'team_id', 'player')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(
        many = True,
        read_only = True
    )
    
    class Meta:
        model = Team
        fields = ('id', 'name', 'region', 'photo_url', 'players')




