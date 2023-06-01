import pytest
from django.contrib.auth.models import User, Permission
from eat_fit_app.models import Recipe, Category, Occasion


@pytest.fixture
def recipes():
    lst = []
    lst.append(
        Recipe.objects.create(name='Dumplings', description='Dumplings with meat', instructions='Make dumplings'))
    lst.append(Recipe.objects.create(name='Tomato soup', description='Healthy tomato soup', instructions='Make soup'))
    lst.append(Recipe.objects.create(name='Eggs', description='Eggs with onion', instructions='Make eggs'))
    return lst


@pytest.fixture
def categories():
    lst = []
    lst.append(Category.objects.create(name='Soups'))
    lst.append(Category.objects.create(name='Breakfast'))
    lst.append(Category.objects.create(name='Main course'))
    return lst


@pytest.fixture
def occasions():
    lst = []
    lst.append(Occasion.objects.create(name='Christmas'))
    lst.append(Occasion.objects.create(name='Birthday'))
    lst.append(Occasion.objects.create(name='Anniversary'))
    return lst


@pytest.fixture
def user_test():
    user = User.objects.create_user(username='test_user', password='test_password',email='test@email.com')
    return user
