from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib import messages
from .forms import RecipeImageUploadForm
from .models import RecipeImage, Recipe


class TestView(View):
    def get(self, request):
        return HttpResponse('WORKING')


class RecipeImageUploadView(View):

    def get(self, request, recipe_id):
        form = RecipeImageUploadForm(recipe_id=recipe_id)
        return render(request, 'add-recipe-image.html', {'form': form, 'recipe_id': recipe_id})

    def post(self, request, recipe_id):
        form = RecipeImageUploadForm(request.POST, request.FILES, recipe_id=recipe_id)
        recipe = get_object_or_404(Recipe, pk=recipe_id)

        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.user = request.user
            recipe_image.save()
            return redirect('recipe-details', recipe_id=recipe_id)
        return render(request, 'add-recipe-image.html', {'form': form, 'recipe_id': recipe_id})


class RecipeImageDeleteView(View):
    def get(self, request, recipe_id, image_id):
        recipe_image = get_object_or_404(RecipeImage, id=image_id, recipe_id=recipe_id)
        if request.user == recipe_image.user or request.user.is_staff:
            recipe_image.delete()
            messages.success(request, "Image deleted successfully")
        else:
            messages.error(request, "Something went wrong with deleting image ")
        return redirect('recipe-edit', recipe_id=recipe_id)
