from django.test import TestCase
from django.contrib.auth.models import User
from eat_fit_app.models import Recipe, Ingredients, RecipeIngredients


class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            user=cls.user
        )

    def test_recipe_creation(self):
        # Test the recipe creation
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.__str__(), 'Test Recipe')
        self.assertEqual(self.recipe.description, 'Test Description')
        self.assertEqual(self.recipe.instructions, 'Test Instructions')

    def test_recipe_user_relation(self):
        # Test the relationship between Recipe and User
        self.assertEqual(self.recipe.user, self.user)

    def test_recipe_fields(self):
        # Test specific fields of Recipe
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertEqual(recipe.name, 'Test Recipe')
        self.assertEqual(recipe.description, 'Test Description')
        self.assertEqual(recipe.instructions, 'Test Instructions')

    def test_recipe_update(self):
        # Test updating Recipe fields
        recipe = Recipe.objects.get(id=self.recipe.id)
        recipe.name = 'Updated Name'
        recipe.save()
        self.assertEqual(recipe.name, 'Updated Name')

