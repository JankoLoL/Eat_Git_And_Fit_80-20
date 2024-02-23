from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from eat_fit_app.models import Recipe, Category, Occasion, Cuisine


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


# class RecipeOccasionListViewTest(ViewTest):
#
#     def test_recipe_occasion_list_view(self):
#         response = self.client.get(reverse('recipes-by-occasion', kwargs={'occasion_id': self.occasion.id}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'app-occasions.html')
#         self.assertTrue('occasion' in response.context)


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

    # def test_recipe_add_view_post(self):
    #     self.client.login(username='testuser', password='testpassword')
    #     response = self.client.post(reverse('recipe-add'), {
    #         'name': 'New Recipe',
    #         'description': 'New Description',
    #         'instructions': 'New Instructions',
    #         'category': "New Category",
    #         'occasion': "New Occasion",
    #         'cuisine': "New Cuisine"
    #     })
    #
    #
