from django.urls import path
from image_handler.views import TestView, RecipeImageUploadView

app_name = 'image_handler'

urlpatterns = [
    path('', TestView.as_view(), name='test_view'),
    path('recipe/image-upload/<int:recipe_id>/', RecipeImageUploadView.as_view(), name='recipe-image-upload')


]
