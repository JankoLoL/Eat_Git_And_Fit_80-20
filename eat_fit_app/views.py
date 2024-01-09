import json

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from eat_fit_app.forms import LoginForm, UserCreateForm, RecipeForm, RecipeIngredientFormSet
from eat_fit_app.models import *
import logging

logger = logging.getLogger(__name__)


class MainView(View):
    def get(self, request):
        return render(request, "index.html")


class RecipeListView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "app-recipes.html", {"recipes": recipes})


class RecipeDetailsView(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        ingredients_list = RecipeIngredients.objects.filter(recipe=recipe)
        recipe_category = RecipeCategory.objects.filter(recipe=recipe)
        recipe_occasion = RecipeOccasion.objects.get(recipe=recipe)

        context = {
            'recipe': recipe,
            'ingredients': ingredients_list,
            'description': recipe.description,
            'instructions': recipe.instructions,
            'category': recipe_category,
            'occasion': recipe_occasion,
        }
        return render(request, "app-recipe-details.html", context=context)


class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, "app-categories.html", {"categories": categories})


class RecipeByCategoryView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        recipes = Recipe.objects.filter(categories=category)
        return render(request, "app-recipes.html", {"recipes": recipes})


class RecipeByOccasionView(View):
    def get(self, request, occasion_id):
        occasion = Occasion.objects.get(id=occasion_id)
        recipes = Recipe.objects.filter(occasions=occasion)
        return render(request, "app-recipes.html", {"recipes": recipes})


class RecipeByCuisineView(View):

    def get(self, request, cuisine_id):
        cuisine = Cuisine.objects.get(id=cuisine_id)
        recipes = Recipe.objects.filter(cuisines=cuisine)
        return render(request, "app-recipes.html", {"recipes": recipes})


class RecipeAddView(View):
    def get(self, request):
        form = RecipeForm()
        formset = RecipeIngredientFormSet()
        return render(request, 'app-recipe-add.html', {'form': form, 'formset': formset})

    def post(self, request):
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            recipe = form.save()
            formset.instance = recipe
            formset.save()
            recipe.user = request.user
            recipe.save()

            recipe.occasions.set(form.cleaned_data['occasion'])
            recipe.categories.set(form.cleaned_data['category'])
            recipe.cuisines.set(form.cleaned_data['cuisine'])
            return redirect('recipe-details', recipe_id=recipe.id)

    # return render(request, 'app-recipe-add.html', {'form': form, 'formset': formset})


# class RecipeAddView(LoginRequiredMixin, View):
#
#     def get(self, request):
#         form = RecipeAddForm()
#         formset = RecipeIngredientsFormset(queryset=RecipeIngredients.objects.none(), prefix='ingredients')
#         return render(request, 'app-recipe-add.html', {'form': form, 'formset': formset})
#
#     def post(self, request):
#         form = RecipeAddForm(request.POST)
#         formset = RecipeIngredientsFormset(request.POST, prefix='ingredients')
#
#         if form.is_valid() and formset.is_valid():
#             recipe = form.save(commit=False)
#             recipe.user = request.user
#             recipe.save()
#
#             recipe.occasions.set(form.cleaned_data['occasion'])
#             recipe.categories.set(form.cleaned_data['category'])
#             recipe.cuisines.set(form.cleaned_data['cuisine'])
#
#             for instance in formset.save(commit=False):
#                 instance.recipe = recipe
#                 instance.save()
#
#             return redirect('recipe-details', recipe_id=recipe.id)
#
#         logger.error("RecipeAddForm Errors: %s", form.errors)
#         logger.error("RecipeIngredientsFormset Errors: %s", formset.errors)
#         return render(request, 'app-recipe-add.html', {'form': form, 'formset': formset})


class RecipeEditView(LoginRequiredMixin, View):

    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(instance=recipe)
        formset = RecipeIngredientFormSet(instance=recipe)

        ingredients = list(Ingredients.objects.values('id', 'name'))
        measures = list(RecipeIngredientsMeasure.objects.values('id', 'measure'))

        return render(request, 'app-recipe-edit.html', {
            'form': form,
            'formset': formset,
            'recipe': recipe,
            'ingredients_json': json.dumps(ingredients),
            'measures_json': json.dumps(measures),
        })

    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(request.POST, instance=recipe)
        formset = RecipeIngredientFormSet(request.POST, instance=recipe)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('recipe-details', recipe_id=recipe.id)
        else:
            ingredients = list(Ingredients.objects.values('id', 'name'))
            measures = list(RecipeIngredientsMeasure.objects.values('id', 'measure'))

            return render(request, 'app-recipe-edit.html', {
                'form': form,
                'formset': formset,
                'recipe': recipe,
                'ingredients_json': json.dumps(ingredients),
                'measures_json': json.dumps(measures),
                'errors': str(form.errors) + str(formset.errors)
            })


class RecipeDeleteView(LoginRequiredMixin, View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return render(request, 'app-recipe-delete.html', {'recipe': recipe})

    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.delete()
        return redirect('recipes')


class OccasionListView(View):
    def get(self, request):
        occasions = Occasion.objects.all()
        return render(request, "app-occasions.html", {"occasions": occasions})


class CuisineListView(View):
    def get(self, request):
        cuisines = Cuisine.objects.all()
        return render(request, "app-cuisines.html", {"cuisines": cuisines})


# ____________LOGIN____________________
class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)
            return redirect(self.request.GET.get('next', 'index'))
        return render(request, 'form.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class CreateUserView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('index')
        return render(request, 'form.html', {'form': form})
