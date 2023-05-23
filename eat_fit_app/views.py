from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from eat_fit_app.models import *


# Create your views here.


# def home(request):
#     return render(request, 'home.html')
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class RecipeListView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "app-recipes.html", {"recipes": recipes})


class RecipeDetailsView(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        # ingredients_list = recipe.ingredients.split(",")
        context = {
            'recipe': recipe,
            # 'ingredients': ingredients_list,
            'description': recipe.description,
        }
        return render(request, "app-recipe-details.html", context=context)


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "app-categories.html", {"categories": categories})
