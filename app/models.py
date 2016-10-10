from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    titles = models.IntegerField()
    crest = models.URLField(max_length=200)
    team_url = models.URLField()

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.IntegerField()
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team)

    def __str__(self):
        return str(self.name)
