"""
URL configuration for eat_fit_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include, re_path
from eat_fit_app.views import RecipeListView, RecipeDetailsView, CategoryListView, RecipeAddView, \
    RecipeEditView, RecipeDeleteView, OccasionListView, MainView, \
    RecipeByCategoryView, RecipeByOccasionView, CuisineListView, RecipeByCuisineView
from eat_fit_django_project import settings

urlpatterns = [

    path('', MainView.as_view() , name='index'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipes/<int:recipe_id>/', RecipeDetailsView.as_view(), name='recipe-details'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('recipes/category/<int:category_id>/', RecipeByCategoryView.as_view(), name='recipes-by-category'),
    path('recipes/occasion/<int:occasion_id>/', RecipeByOccasionView.as_view(), name='recipes-by-occasion'),
    path('recipes/cuisine/<int:cuisine_id>/', RecipeByCuisineView.as_view(), name='recipes-by-cuisine'),
    path('recipe/add/', RecipeAddView.as_view(), name='recipe-add'),
    path('recipe/edit/<int:recipe_id>/', RecipeEditView.as_view(), name='recipe-edit'),
    path('recipe/delete/<int:recipe_id>/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('occasions/', OccasionListView.as_view(), name='occasions'),
    path('cuisine/', CuisineListView.as_view(), name='cuisines'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)