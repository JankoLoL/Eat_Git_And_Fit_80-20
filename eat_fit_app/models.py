from django.db import models


# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    recipe_ingredients = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe, through='RecipeCategory', related_name='categories')

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name


class Ingredients(models.Model):
    name = models.CharField(max_length=128)
    recipe = models.ManyToManyField(Recipe, through='RecipeIngredients', related_name='ingredients')

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    measure = models.CharField(max_length=64)

    def __str__(self):
        return self.ingredients.name


class Occasion(models.Model):
    name = models.CharField(max_length=128, default='')
    description = models.TextField(max_length=128)
    recipes = models.ManyToManyField(Recipe, through='RecipeOccasion', related_name='occasions')

    def __str__(self):
        return self.name


class RecipeOccasion(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.occasion.name


class Cuisine(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe, through='RecipeCuisine', related_name='cuisines')

    def __str__(self):
        return self.name


class RecipeCuisine(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    def __str__(self):
        return self.cuisine.name
