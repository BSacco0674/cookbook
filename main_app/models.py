from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS = (
    ('1', '⭐️'),
    ('2', '⭐️⭐️'),
    ('3', '⭐️⭐️⭐️'),
    ('4', '⭐️⭐️⭐️⭐️'),
    ('5', '⭐️⭐️⭐️⭐️⭐️')
)

class Recipe(models.Model):
    name = models.CharField('Recipe Name:', max_length=100)
    ingredients = models.TextField('Ingredients: (comma separate items', max_length=250)
    instructions = models.TextField('Directions: (write complete sentences)', max_length=900)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'recipe_id': self.id})

class Review(models.Model):
    rating = models.CharField(
        max_length=1,
        choices=RATINGS,
        default=RATINGS[0][0]
    )
    comment = models.TextField(max_length=250)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment}"

class Modification(models.Model):
    content = models.TextField(max_length=250)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"

    