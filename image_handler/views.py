from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .forms import RecipeImageUploadForm
from .models import RecipeImage, Recipe


class TestView(View):
    def get(self, request):
        return HttpResponse('WORKING')


class RecipeImageUploadView(View):

    def get(self, request, recipe_id):
        form = RecipeImageUploadForm()
        return render(request, 'add-recipe-image.html', {'form': form, 'recipe_id': recipe_id})

    def post(self, request, recipe_id):
        form = RecipeImageUploadForm(request.POST, request.FILES)
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        if form.is_valid():
            print("Form data:", form.cleaned_data)

            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.user = request.user
            recipe_image.save()
            return redirect('recipe-details', recipe_id=recipe_id)
        return render(request, 'add-recipe-image.html', {'form': form, 'recipe_id': recipe_id })
