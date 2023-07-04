# Generated by Django 4.2 on 2023-06-06 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eat_fit_app', '0005_remove_recipe_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredientsMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='recipeingredients',
            name='measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eat_fit_app.recipeingredientsmeasure'),
        ),
    ]