from django.contrib import admin
from .models import Team, Player, Conference
admin.site.register(Conference)
admin.site.register(Team)
admin.site.register(Player)