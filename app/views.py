from django.shortcuts import render
from app.models import Player, Team
# Create your views here.


def index_view(request):

    return render(request, "index.html")


def favorite_players_view(request):
    context = {
        "fav_players": Player.objects.all()
    }
    return render(request, "favorite_players.html", context)


def player_view(request, player_id):
    context = {
        "player": Player.objects.get(id=player_id),
    }
    return render(request, "player.html", context)


def teams_view(request):
    context = {
        "all_teams": Team.objects.all()
    }
    return render(request, "teams.html", context)


def team_view(request, team_id):
    context = {
        "team": Team.objects.get(id=team_id)
    }

    return render(request, "team.html", context)


def about_me_view(request):

    return render(request, "about_me.html")
