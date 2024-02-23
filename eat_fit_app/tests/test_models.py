from django.test import TestCase
from django.contrib.auth.models import User
from eat_fit_app.models import Recipe, Ingredients, RecipeIngredients, Category, RecipeIngredientsMeasure, \
    RecipeCategory, Occasion, Cuisine


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
        cls.ingredient = Ingredients.objects.create(name='Tomato')
        RecipeIngredients.objects.create(recipe=cls.recipe, ingredients=cls.ingredient, quantity=3)




    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(self.recipe.__str__(), 'Test Recipe')
        self.assertEqual(self.recipe.description, 'Test Description')
        self.assertEqual(self.recipe.instructions, 'Test Instructions')

    def test_recipe_deletion(self):
        self.assertEqual(RecipeIngredients.objects.count(), 1)
        self.recipe.delete()
        self.assertEqual(RecipeIngredients.objects.count(), 0)

    def test_recipe_user_relation(self):
        self.assertEqual(self.recipe.user, self.user)

    def test_recipe_fields(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        self.assertEqual(recipe.name, 'Test Recipe')
        self.assertEqual(recipe.description, 'Test Description')
        self.assertEqual(recipe.instructions, 'Test Instructions')

    def test_recipe_update(self):
        recipe = Recipe.objects.get(id=self.recipe.id)
        recipe.name = 'Updated Name'
        recipe.save()
        self.assertEqual(recipe.name, 'Updated Name')


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='Dessert', description='Sweet food')

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), 'Dessert')
        self.assertEqual(self.category.description, 'Sweet food')


class IngredientsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ingredient = Ingredients.objects.create(name='Sugar')

    def test_ingredient_creation(self):
        self.assertTrue(isinstance(self.ingredient, Ingredients))
        self.assertEqual(self.ingredient.__str__(), 'Sugar')


class RecipeIngredientsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser2', password='12345')
        recipe = Recipe.objects.create(name='Cake', description='Delicious cake', user=user)
        ingredient = Ingredients.objects.create(name='Flour')
        measure = RecipeIngredientsMeasure.objects.create(measure='Cups')
        cls.recipe_ingredient = RecipeIngredients.objects.create(
            recipe=recipe,
            ingredients=ingredient,
            quantity=2,
            measure=measure
        )

    def test_recipe_ingredient_creation(self):
        self.assertTrue(isinstance(self.recipe_ingredient, RecipeIngredients))
        self.assertEqual(self.recipe_ingredient.quantity, 2)
        self.assertEqual(self.recipe_ingredient.measure.measure, 'Cups')


class RecipeCategoryRelationTest(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(name='Salad', description='Fresh salad')
        self.category = Category.objects.create(name='Healthy', description='Healthy food')

    def test_recipe_category_relation(self):
        RecipeCategory.objects.create(recipe=self.recipe, category=self.category)
        self.assertEqual(self.recipe.categories.first().name, 'Healthy')
        self.assertEqual(self.category.recipes.first().name, 'Salad')


class OccasionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.occasion = Occasion.objects.create(name='Birthday', description='Birthday party food')

    def test_occasion_creation(self):
        self.assertTrue(isinstance(self.occasion, Occasion))
        self.assertEqual(self.occasion.__str__(), 'Birthday')
        self.assertEqual(self.occasion.description, 'Birthday party food')


class CuisineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cuisine = Cuisine.objects.create(name='Italian', description='Italian cuisine')

    def test_cuisine_creation(self):
        self.assertTrue(isinstance(self.cuisine, Cuisine))
        self.assertEqual(self.cuisine.__str__(), 'Italian')
        self.assertEqual(self.cuisine.description, 'Italian cuisine')
