from django.db import models
from authsys.models import *


class Ability(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')


class CardClass(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=500, default='')


class Card(models.Model):
    user_profiles = models.ManyToManyField(UserProfile)
    name = models.CharField(max_length=50, default="")
    mana = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    abilities = models.ManyToManyField(Ability, blank=True, null=True)
    card_class = models.ForeignKey(CardClass, blank=True, null=True, on_delete=models.SET_NULL)
    img = models.CharField(max_length=100, default='')


class Deck(models.Model):
    name = models.CharField(max_length=30, default='')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
