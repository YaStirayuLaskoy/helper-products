# Generated by Django 3.2.16 on 2023-08-21 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название Ингредиента', max_length=50, verbose_name='Название ингредиента')),
                ('count', models.PositiveIntegerField()),
                ('unit', models.CharField(choices=[('g', 'г'), ('kg', 'кг'), ('l', 'л'), ('ml', 'мл'), ('tbl.s.', 'ст.л.'), ('shtuka', 'шт'), ('pinch', 'щепотка'), ('taste', 'по вкусу')], help_text='Введите единицу измерения', max_length=10, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название тега', max_length=50, unique=True, verbose_name='Название тега')),
                ('slug', models.SlugField(help_text='Введите какое-то слаг значение', unique=True, verbose_name='Какое-то слаг значение')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название рецепта', max_length=90, verbose_name='Название рецепта')),
                ('image', models.ImageField(help_text='Загрузите изображение рецепта', null=True, upload_to='backend/foodgram_backend/', verbose_name='Изображение рецепта')),
                ('text', models.TextField(help_text='Введите рецепт', max_length=2500, unique=True, verbose_name='Описание рецепта')),
                ('cooking_time', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта')),
                ('ingredient', models.ManyToManyField(to='recipes.Ingredient')),
                ('tag', models.ManyToManyField(to='recipes.Tag')),
            ],
        ),
    ]
