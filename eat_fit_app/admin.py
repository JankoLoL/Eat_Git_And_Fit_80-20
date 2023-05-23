from django.contrib import admin
from .models import Recipe, Category, RecipeCategory, Ingredients, RecipeIngredients, Occasion, RecipeOccasion,\
    Cuisine, RecipeCuisine
# Register your models here.



models_to_register = [Recipe, Category, RecipeCategory, Ingredients, RecipeIngredients, Occasion, RecipeOccasion,
                      Cuisine, RecipeCuisine]


for model in models_to_register:
    admin.site.register(model)
