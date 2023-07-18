from rest_framework import serializers
from.models import *




class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team-detail',
        read_only=True
    )

    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )

    class Meta:
        model = Player
        fields = ('id', 'photo_url', 'name', 'position', 'age', 'on_injured_reserved_list', 'team', 'team_id')




class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = serializers.HyperlinkedRelatedField(
        view_name='player_detail',
        many=True,
        read_only=True
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team-detail'
    )

    class Meta:
        model = Team
        fields = ('id', 'team_url', 'players', 'name', 'location', 'division', 'number_of_wins', 'number_of_losses', 'team_logo_url')



