import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from eat_fit_app.forms import RecipeForm, RecipeIngredientFormSet, IngredientForm
from eat_fit_app.models import Recipe, Category, Occasion, Cuisine, RecipeCategory, RecipeOccasion, RecipeCuisine, \
    Ingredients, RecipeIngredientsMeasure
import logging

logger = logging.getLogger(__name__)


class MainView(View):
    def get(self, request):
        return render(request, "index.html")


class RecipeListView(View):

    def get(self, request):
        recipes = Recipe.objects.prefetch_related('recipe_images').all()

        for recipe in recipes:
            main_image = recipe.recipe_images.filter(type='main_image').first()
            recipe.main_image_url = main_image.image_file.url if main_image else None

        return render(request, "app-recipes.html", {"recipes": recipes})


class RecipeDetailsView(View):
    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        main_image = recipe.recipe_images.filter(type='main_image').first()
        additional_images = recipe.recipe_images.filter(type='additional_image').all()

        context = {
            'recipe': recipe,
            'main_image': main_image,
            'additional_images': additional_images,
            'ingredients': recipe.recipeingredients_set.all(),
            'categories': recipe.categories.all(),
            'occasions': recipe.occasions.all(),
            'cuisines': recipe.cuisines.all(),
        }
        return render(request, "app-recipe-details.html", context)


class UserRecipeListVew(LoginRequiredMixin, View):
    def get(self, request):
        user_recipes = Recipe.objects.filter(user=request.user).prefetch_related('recipe_images')

        for recipe in user_recipes:
            main_image = recipe.recipe_images.filter(type='main_image').first()
            recipe.main_image_url = main_image.image_file.url if main_image else None
        return render(request, "user-recipes.html", {"recipes": user_recipes})


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


class RecipeAddView(LoginRequiredMixin, View):

    def handle_no_permission(self):
        messages.info(self.request, "Please login to add a recipe")
        return super().handle_no_permission()

    def get(self, request):

        form = RecipeForm()
        formset = RecipeIngredientFormSet()
        return render(request, 'app-recipe-add.html', {'form': form, 'formset': formset})

    def post(self, request):
        form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            RecipeCategory.objects.create(recipe=recipe, category=form.cleaned_data['category'])
            RecipeOccasion.objects.create(recipe=recipe, occasion=form.cleaned_data['occasion'])
            RecipeCuisine.objects.create(recipe=recipe, cuisine=form.cleaned_data['cuisine'])

            formset.instance = recipe
            if formset.is_valid():
                formset.save()
                return redirect('recipe-details', recipe_id=recipe.id)
            else:
                print("Form errors:", formset.errors)

        if not form.is_valid():
            print("Form errors:", form.errors)

        return render(request, 'app-recipe-add.html', {'form': form, 'formset': formset})


class RecipeEditView(LoginRequiredMixin, View):

    def get(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(instance=recipe)
        formset = RecipeIngredientFormSet(instance=recipe)

        ingredients = list(Ingredients.objects.values('id', 'name'))
        measures = list(RecipeIngredientsMeasure.objects.values('id', 'measure'))

        if not (request.user == recipe.user or request.user.is_staff):
            messages.error(request, "You do not have permission to edit this recipe.")
            return redirect('recipe-details', recipe_id=recipe.id)

        return render(request, 'app-recipe-edit.html', {
            'form': form,
            'formset': formset,
            'recipe': recipe,
            'ingredients_json': json.dumps(ingredients),
            'measures_json': json.dumps(measures),
        })

    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, id=recipe_id)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        formset = RecipeIngredientFormSet(request.POST, instance=recipe)

        if not (request.user == recipe.user or request.user.is_staff):
            messages.error(request, "You do not have permission to edit this recipe.")
            return redirect('recipe-details', recipe_id=recipe.id)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Recipe updated successfully.")
            return redirect('recipe-details', recipe_id=recipe.id)
        else:
            messages.error(request, "There was an error with your submission. Please check the form.")
            return render(request, 'app-recipe-edit.html', {
                'form': form,
                'formset': formset,
                'recipe': recipe,
            })


class RecipeDeleteView(LoginRequiredMixin, View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        return render(request, 'app-recipe-delete.html', {'recipe': recipe})

    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.delete()
        return redirect('recipes')


class IngredientAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = IngredientForm
        return render(request, 'app-ingredient-add.html', {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ingredient added successfully.")
            return redirect('ingredient-add')
        else:
            messages.error(request, "There was an error with your submission")
            return render(request, 'app-ingredient-add.html', {'form': form})


class OccasionListView(View):
    def get(self, request):
        occasions = Occasion.objects.all()
        return render(request, "app-occasions.html", {"occasions": occasions})


class CuisineListView(View):
    def get(self, request):
        cuisines = Cuisine.objects.all()
        return render(request, "app-cuisines.html", {"cuisines": cuisines})
