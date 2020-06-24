from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=250)
    instructions = models.TextField(max_length=900)

    def __str__(self):
        return self.name
    
  # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(max_length=250)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment}"

class Modification(models.Model):
    content = models.TextField(max_length=250)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"