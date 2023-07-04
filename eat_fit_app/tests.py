from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
import pytest
from django.test import Client
from django.urls import reverse
from eat_fit_app.forms import RecipeAddForm, LoginForm
from eat_fit_app.models import Recipe, Category, Occasion, RecipeCategory, RecipeOccasion


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
    result = [item in response.context['recipes'] for item in recipes]
    assert all(result)

    # for item in recipes:
    #     assert item in response.context['recipes']


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
    result = [item in response.context['categories'] for item in categories]
    assert all(result)


@pytest.mark.django_db
def test_recipe_by_category(recipes, categories):
    client = Client()
    category = categories[0]
    url = reverse('recipes-by-category', args=[category.id])
    response = client.get(url)
    assert response.status_code == 200
    recipes_by_category = RecipeCategory.objects.filter(category=category)
    result = [item in response.context['recipes_by_category'] for item in recipes_by_category]
    assert all(result)



@pytest.mark.django_db
def test_recipe_by_occasion(recipes, occasions):
    client = Client()
    occasion = occasions[0]
    url = reverse('recipes-by-occasion', args=[occasion.id])
    response = client.get(url)
    assert response.status_code == 200
    recipes_by_occasion = RecipeOccasion.objects.filter(occasion=occasion)
    result = [item in response.context['recipes_by_occasion'] for item in recipes_by_occasion]
    assert all(result)


@pytest.mark.django_db
def test_add_recipe_get():
    client = Client()
    url = reverse('recipe-add')
    response = client.get(url)
    assert response.status_code == 302


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


@pytest.mark.django_db
def test_edit_recipe_get():
    client = Client()
    url = reverse('recipe-edit', args=[1])
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_edit_recipe_post():
    client = Client()
    url = reverse('recipe-edit', args=[1])
    data = {
        'name': 'ppp'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))
    try:
        recipe = Recipe.objects.filter(id=1).exists()
        assert recipe is not None
    except ObjectDoesNotExist:
        pytest.fail("Recipe 'ppp' was not created")


@pytest.mark.django_db
def test_delete_recipe_get():
    client = Client()
    url = reverse('recipe-delete', args=[1])
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))


@pytest.mark.django_db
def test_delete_recipe_post():
    client = Client()
    url = reverse('recipe-delete', args=[1])
    response = client.post(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))
    try:
        recipe = Recipe.objects.filter(id=1).exists()
        assert recipe is not None
    except ObjectDoesNotExist:
        pytest.fail("Can not delete, recipe was not found in database")


@pytest.mark.django_db
def test_occasion_list(occasions):
    client = Client()
    url = reverse('occasions')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['occasions'].count() == len(occasions)
    for item in occasions:
        assert item in response.context['occasions']


@pytest.mark.django_db
def test_login_get():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['form'] is not None


@pytest.mark.django_db
def test_login_post():
    client = Client()
    url = reverse('login')
    assert client.login(username='admin', password='admin') is False
    form_data = {'username': 'admin', 'password': 'admin'}
    response = client.post(url, form_data)
    assert response.status_code == 200
    assert response.context['form'] is not None
    assert response.context['form'].is_valid() is False
    assert response.context['form'].errors is not None


@pytest.mark.django_db
def test_logout():
    client = Client()
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('index'))


@pytest.mark.django_db
def test_register_get():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['form'] is not None


@pytest.mark.django_db
def test_register_post():
    client = Client()
    url = reverse('register')
    form_data = {
        'username': 'admin',
        'password1': 'admin',
        'password2': 'admin',
        'email': 'aa@gmail.com'
    }
    response = client.post(url, form_data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('index'))
    try:
        user = User.objects.get(username='admin')
        assert user is not None
    except ObjectDoesNotExist:
        pytest.fail("User 'admin' was not created")



@pytest.mark.django_db
def test_create_user_get():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['form'] is not None


@pytest.mark.django_db
def test_create_user_post(user_test):
    assert user_test is not None
    assert user_test.username == 'test_user'
    assert user_test.email == 'test@email.com'
    assert user_test.password is not None






