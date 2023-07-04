from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from eat_fit_app.forms import RecipeAddForm, LoginForm, UserCreateForm
from eat_fit_app.models import *


# Create your views here.


# def home(request):
#     return render(request, 'home.html')
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


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


class RecipeAddView(LoginRequiredMixin, View):

    def get(self, request):
        # if not request.user.is_authenticated:
        #     return redirect('login')
        form = RecipeAddForm()
        return render(request, 'app-recipe-add.html', {'form': form})

    def post(self, request):
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe-details', recipe_id=recipe.id)


class RecipeEditView(LoginRequiredMixin,View):

    def get(self, request, recipe_id):
        # if not request.user.is_authenticated:
        #     return redirect('login')
        recipe = Recipe.objects.get(id=recipe_id)
        form = RecipeAddForm(instance=recipe)
        return render(request, 'app-recipe-edit.html', {'form': form, 'recipe': recipe})

    def post(self, request, recipe_id):
        recipe = Recipe.objects.get(id=recipe_id)
        form = RecipeAddForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe-details', recipe_id=recipe_id)
        else:
            return render(request, 'app-recipe-edit.html', {'form': form, 'recipe': recipe})


class RecipeDeleteView(LoginRequiredMixin,View):
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
