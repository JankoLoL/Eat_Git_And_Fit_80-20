# Generated by Django 4.2.1 on 2024-03-26 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eat_fit_app', '0007_recipe_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['created']},
        ),
    ]
