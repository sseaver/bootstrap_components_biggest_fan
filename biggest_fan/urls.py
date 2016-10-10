"""biggest_fan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import index_view, favorite_players_view, player_view, teams_view, team_view, about_me_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index_view"),
    url(r'^favorite_players/$', favorite_players_view, name="favorite_players"),
    url(r'^player/(?P<player_id>\d+)/$', player_view, name="player_view"),
    url(r'^teams/$', teams_view, name="teams_view"),
    url(r'^team/(?P<team_id>\d+)/$', team_view, name="team_view"),
    url(r'^about_me/$', about_me_view, name="about_me"),

]
