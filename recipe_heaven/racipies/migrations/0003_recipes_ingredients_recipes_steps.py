# Generated by Django 5.1.5 on 2025-01-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racipies', '0002_recipes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipes',
            name='steps',
            field=models.TextField(blank=True),
        ),
    ]
