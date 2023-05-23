from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from eat_fit_app.models import *

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class RecipeListView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "app-recipes.html", {"recipes": recipes})



