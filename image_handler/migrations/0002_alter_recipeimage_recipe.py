# Generated by Django 4.2.1 on 2024-01-09 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eat_fit_app', '0006_recipeingredientsmeasure_and_more'),
        ('image_handler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeimage',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_images', to='eat_fit_app.recipe'),
        ),
    ]
