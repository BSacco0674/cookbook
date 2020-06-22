from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=250)
    instructions = models.TextField(max_length=900)

class Reviews(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(max_length=250)
    modifications = models.TextField(max_length=250)