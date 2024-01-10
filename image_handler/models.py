from django.db import models
from django.contrib.auth.models import User

from eat_fit_app.models import Recipe


def recipe_image_directory_path(instance, filename):
    return f'recipes/{instance.recipe.id}/{filename}'


class RecipeImage(models.Model):
    TYPE_CHOICES = [
        ('main_image', 'Main Image'),
        ('additional_image', 'Additional Image'),
    ]
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_images", blank=True, null=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    description = models.TextField()
    alt_description = models.CharField(max_length=256, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_images")
    image_file = models.ImageField(upload_to=recipe_image_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image name: {self.name} for recipe {self.recipe} added by {self.user}"
