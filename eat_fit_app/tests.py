from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from eat_fit_app.forms import RecipeAddForm
from eat_fit_app.models import Recipe, Category, Occasion


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_recipes_list(recipes):
    client = Client()
    url = reverse('recipes')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['recipes'].count() == len(recipes)
    for item in recipes:
        assert item in response.context['recipes']


@pytest.mark.django_db
def test_recipe_details(recipes):
    client = Client()
    recipe = recipes[0]
    url = reverse('recipe-details', args=[recipe.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['recipe'] == recipe
    assert response.context['recipe'].name == recipe.name


@pytest.mark.django_db
def test_categories_list(categories):
    client = Client()
    url = reverse('categories')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['categories'].count() == len(categories)
    for item in categories:
        assert item in response.context['categories']


@pytest.mark.django_db
def test_recipe_by_category(recipes, categories):
    client = Client()
    category = categories[0]
    url = reverse('recipes-by-category', args=[category.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_recipe_by_occasion(recipes, occasions):
    client = Client()
    occasion = occasions[0]
    url = reverse('recipes-by-occasion', args=[occasion.id])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_recipe_get():
    client = Client()
    url = reverse('recipe-add')
    response = client.get(url)
    assert response.status_code == 302




import pytest
from django.test import Client
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

@pytest.mark.django_db
def test_add_recipe_post():
    client = Client()
    url = reverse('recipe-add')
    data = {
        'name': 'ppp'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))
    try:
        recipe = Recipe.objects.filter(name='ppp').exists()
        assert recipe is not None
    except ObjectDoesNotExist:
        pytest.fail("Recipe 'ppp' was not created")
