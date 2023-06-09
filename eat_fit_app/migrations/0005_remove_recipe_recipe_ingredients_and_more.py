# Generated by Django 4.2 on 2023-06-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat_fit_app', '0004_remove_recipe_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.ManyToManyField(related_name='recipes', through='eat_fit_app.RecipeIngredients', to='eat_fit_app.ingredients'),
        ),
    ]
