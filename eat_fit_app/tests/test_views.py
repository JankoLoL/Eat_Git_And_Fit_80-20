from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from eat_fit_app.models import Recipe, Category, Occasion, Cuisine, RecipeOccasion, Ingredients, \
    RecipeIngredientsMeasure, RecipeIngredients


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='Test Description',
            instructions='Test Instructions',
            user=self.user
        )
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.occasion = Occasion.objects.create(name='Test Occasion', description='Test Description')
        self.cuisine = Cuisine.objects.create(name='Test Cuisine', description='Test Description')
        self.ingredient = Ingredients.objects.create(name='Test Ingredient')
        self.measure = RecipeIngredientsMeasure.objects.create(measure='Test Measure')


class MainViewTest(ViewTest):
    def test_main_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class RecipeListViewTest(ViewTest):
    def test_recipe_list_view(self):
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app-recipes.html')
        self.assertTrue('recipes' in response.context)


class RecipeOccasionListViewTest(ViewTest):

    def test_recipe_occasion_list_view(self):
        response = self.client.get(reverse('recipes-by-occasion', kwargs={'occasion_id': self.occasion.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app-recipes.html')

        filtered_recipes = response.context['recipes']
        for recipe in filtered_recipes:
            self.assertIn(self.occasion, recipe.occasions.all())

    def test_occasion_selection_redirect(self):
        RecipeOccasion.objects.create(recipe=self.recipe, occasion=self.occasion)
        response = self.client.get(reverse('recipes-by-occasion', kwargs={'occasion_id': self.occasion.id}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app-recipes.html')
        self.assertTrue('recipes' in response.context)
        filtered_recipes = response.context['recipes']
        self.assertEqual(filtered_recipes.count(), 1)


class RecipeDetailsViewTest(ViewTest):
    def test_recipe_details_view(self):
        response = self.client.get(reverse('recipe-details', kwargs={'recipe_id': self.recipe.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app-recipe-details.html')
        self.assertTrue('recipe' in response.context)


class UserRecipeListViewTest(ViewTest):
    def test_user_recipe_list_view_not_logged_in(self):
        response = self.client.get(reverse('my-recipes'))
        self.assertRedirects(response, f'/user/login/?next={reverse("my-recipes")}')

    def test_user_recipe_list_view_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/my-recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-recipes.html')


class RecipeAddViewTest(ViewTest):
    def test_recipe_add_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipe-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app-recipe-add.html')

    def test_recipe_add_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('recipe-add')
        recipe_data = {
            'name': 'New Test Recipe',
            'description': 'New Description',
            'instructions': 'New Instructions',
            'category': self.category.id,
            'occasion': self.occasion.id,
            'cuisine': self.cuisine.id,
        }

        ingredient_formset_data = {
            'recipeingredients_set-TOTAL_FORMS': '1',
            'recipeingredients_set-INITIAL_FORMS': '0',
            'recipeingredients_set-MIN_NUM_FORMS': '0',
            'recipeingredients_set-MAX_NUM_FORMS': '1000',

            'recipeingredients_set-0-ingredient': self.ingredient.id,
            'recipeingredients_set-0-quantity': '2',
            'recipeingredients_set-0-measure': self.measure.id,
        }

        post_data = {**recipe_data, **ingredient_formset_data}
        response = self.client.post(url, post_data)

        if response.status_code != 302:
            print("Form errors in response:", response.context.get('form_errors', 'No form errors'))
            print("Formset errors in response:", response.context.get('formset_errors', 'No formset errors'))

        self.assertEqual(response.status_code, 302)
