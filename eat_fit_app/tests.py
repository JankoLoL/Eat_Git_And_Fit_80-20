from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from eat_fit_app.forms import RecipeAddForm
from eat_fit_app.models import Recipe, Category


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