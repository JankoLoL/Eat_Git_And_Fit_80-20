from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=128)
    recipe_ingredients = models.ManyToManyField('Ingredients', through='RecipeIngredients', related_name='recipes')
    description = models.TextField()
    instructions = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='recipes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('recipe-details', args=[str(self.id)])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe, through='RecipeCategory', related_name='categories')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Recipe Categories'

    def __str__(self):
        return self.category.name


class Ingredients(models.Model):
    name = models.CharField(max_length=128)
    recipe = models.ManyToManyField(Recipe, through='RecipeIngredients', related_name='ingredients')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients_relation')
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name='recipe_relation')
    quantity = models.IntegerField()
    measure = models.ForeignKey('RecipeIngredientsMeasure', on_delete=models.CASCADE, null=True,
                                related_name='quantity_measurements')

    class Meta:
        verbose_name_plural = 'Recipe Ingredients'

    def __str__(self):
        return f' Recipe: {self.recipe.name}| Ingredient: {self.ingredients.name}| Quantity: {self.quantity}'


class RecipeIngredientsMeasure(models.Model):
    measure = models.CharField(max_length=64)

    def __str__(self):
        return self.measure


class Occasion(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    recipes = models.ManyToManyField(Recipe, through='RecipeOccasion', related_name='occasions')

    class Meta:
        verbose_name_plural = 'Occasions'

    def __str__(self):
        return self.name


class RecipeOccasion(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Recipe Occasions'

    def __str__(self):
        return self.occasion.name


class Cuisine(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    recipes = models.ManyToManyField(Recipe, through='RecipeCuisine', related_name='cuisines')

    class Meta:
        verbose_name_plural = 'Cuisines'

    def __str__(self):
        return self.name


class RecipeCuisine(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Recipe Cuisines'

    def __str__(self):
        return self.cuisine.name
