# Generated by Django 3.0.1 on 2022-03-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VictoryApp', '0010_auto_20220317_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Creado'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Creado'),
        ),
    ]