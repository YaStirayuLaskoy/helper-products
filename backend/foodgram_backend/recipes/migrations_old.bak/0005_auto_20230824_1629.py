# Generated by Django 3.2.16 on 2023-08-24 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20230824_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='collor',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]