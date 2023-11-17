from rest_framework import serializers
from .models import Team, Player, Conference

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset = Team.objects.all(),
        source='team'
    )
    class Meta:
        model = Player
        fields = ('id', 'team', 'team_id', 'name', 'position', 'age', 'injured', 'number', 'college')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(
        many=True,
        read_only=True
    )

    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team_detail'
    )
    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'division', 'wins', 'losses', 'players', 'team_url')

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = TeamSerializer(
        many=True,
        read_only=True
    )

    conference_url = serializers.ModelSerializer.serializer_url_field(
        view_name='conference_detail'
    )
    class Meta:
        model = Conference
        fields = ('name', 'teams', 'conference_url')