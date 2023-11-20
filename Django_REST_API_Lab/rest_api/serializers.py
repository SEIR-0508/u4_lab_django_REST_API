# serializers.py
# from rest_framework import serializers
# from .models import Team, Player

# class TeamSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Team
#         fields = ('id', 'name', 'location', 'division', 'wins', 'losses')

# class PlayerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Player
#         fields = ('id', 'name', 'position', 'age', 'injured_reserved', 'team')

from rest_framework import serializers
from .models import Team, Player
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name ="Team_detail",
        read_only = True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )
    class Meta:
        model = Player
        fields = ('id', 'name', 'position', 'age', 'injured_reserved', 'team', 'team_id')
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(
        many=True,
        read_only=True
    )
    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='Team_detail'
    )
    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'division', 'wins', 'losses', 'team_url', 'players') 
