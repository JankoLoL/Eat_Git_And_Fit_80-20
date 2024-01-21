from django.urls import path
from image_handler.views import TestView, RecipeImageUploadView, RecipeImageDeleteView

app_name = 'image_handler'

urlpatterns = [
    path('', TestView.as_view(), name='test_view'),
    path('recipe/image-upload/<int:recipe_id>/', RecipeImageUploadView.as_view(), name='recipe-image-upload'),
    path('recipe/<int:recipe_id>/delete-image/<int:image_id>/', RecipeImageDeleteView.as_view(),
         name='recipe-image-delete'),

]
