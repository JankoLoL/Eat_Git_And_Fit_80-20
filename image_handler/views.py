from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import RecipeImageUploadForm

class TestView(View):
    def get(self, request):
        return HttpResponse('WORKING')


class RecipeImageUpload(View):

    def get(self, request):
        form = RecipeImageUploadForm
        return render(request, 'add-recipe-image.html', {'form': form} )

    def post(self, request):
        form = RecipeImageUploadForm(request.POST)

        if form.is_valid():
            form.save()


