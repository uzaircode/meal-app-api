# Generated by Django 3.2.20 on 2023-07-25 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='user',
        ),
    ]
