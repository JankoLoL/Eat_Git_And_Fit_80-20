# Generated by Django 4.2.1 on 2024-01-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_handler', '0003_alter_recipeimage_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeimage',
            name='alt_description',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
    ]
