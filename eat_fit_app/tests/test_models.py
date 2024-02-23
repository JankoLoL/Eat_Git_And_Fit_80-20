from django.test import TestCase
from django.contrib.auth.models import User
from eat_fit_app.models import Recipe, Ingredients, RecipeIngredients, Category, RecipeIngredientsMeasure, \
    RecipeCategory, Occasion, Cuisine, RecipeOccasion, RecipeCuisine


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')

        cls.ingredient_tomato = Ingredients.objects.create(name='Tomato')
        cls.ingredient_sugar = Ingredients.objects.create(name='Sugar')

        cls.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            user=cls.user
        )

        cls.recipe_ingredient = RecipeIngredients.objects.create(
            recipe=cls.recipe,
            ingredients=cls.ingredient_tomato,
            quantity=3,
            measure=RecipeIngredientsMeasure.objects.create(measure='Cups')
        )

        cls.category = Category.objects.create(name='Dessert', description='Sweet food')

        cls.occasion = Occasion.objects.create(name='Birthday', description='Birthday party food')

        cls.cuisine = Cuisine.objects.create(name='Italian', description='Italian cuisine')

        RecipeCategory.objects.create(recipe=cls.recipe, category=cls.category)
        RecipeOccasion.objects.create(recipe=cls.recipe, occasion=cls.occasion)


class RecipeModelTest(BaseTest):
    def test_recipe_creation(self):
        self.assertTrue(isinstance(self.recipe, Recipe))
        self.assertEqual(str(self.recipe), 'Test Recipe')

    def test_recipe_deletion(self):
        self.assertEqual(RecipeIngredients.objects.count(), 1)
        self.recipe.delete()
        self.assertEqual(RecipeIngredients.objects.count(), 0)

    def test_recipe_user_relation(self):
        self.assertEqual(self.recipe.user, self.user)

    def test_recipe_fields(self):
        self.assertEqual(self.recipe.name, 'Test Recipe')
        self.assertEqual(self.recipe.description, 'Test Description')

    def test_recipe_update(self):
        self.recipe.name = 'Updated Name'
        self.recipe.save()
        self.assertEqual(self.recipe.name, 'Updated Name')


class CategoryModelTest(BaseTest):
    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(str(self.category), 'Dessert')


class IngredientsModelTest(BaseTest):
    def test_ingredient_creation(self):
        self.assertTrue(isinstance(self.ingredient_tomato, Ingredients))
        self.assertEqual(str(self.ingredient_tomato), 'Tomato')


class RecipeIngredientsModelTest(BaseTest):
    def test_recipe_ingredient_creation(self):
        self.assertTrue(isinstance(self.recipe_ingredient, RecipeIngredients))
        self.assertEqual(self.recipe_ingredient.quantity, 3)
        self.assertEqual(self.recipe_ingredient.measure.measure, 'Cups')


class RecipeCategoryRelationTest(BaseTest):
    def test_recipe_category_relation(self):
        self.assertIn(self.category, self.recipe.categories.all())


class OccasionModelTest(BaseTest):
    def test_occasion_creation(self):
        self.assertTrue(isinstance(self.occasion, Occasion))
        self.assertEqual(str(self.occasion), 'Birthday')


class CuisineModelTest(BaseTest):
    def test_cuisine_creation(self):
        self.assertTrue(isinstance(self.cuisine, Cuisine))
        self.assertEqual(str(self.cuisine), 'Italian')


# Additional Tests
class RecipeOccasionRelationTest(BaseTest):
    def test_recipe_occasion_relation(self):
        self.assertIn(self.occasion, self.recipe.occasions.all())


class RecipeCuisineRelationTest(BaseTest):
    def setUp(self):
        self.new_recipe = Recipe.objects.create(
            name='Pizza',
            description='Italian pizza',
            instructions='Bake for 20 minutes',
            user=self.user
        )
        RecipeCuisine.objects.create(recipe=self.new_recipe, cuisine=self.cuisine)

    def test_recipe_cuisine_relation(self):
        self.assertIn(self.cuisine, self.new_recipe.cuisines.all())
        self.assertIn(self.new_recipe, self.cuisine.recipes.all())
