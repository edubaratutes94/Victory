# Generated by Django 3.0.1 on 2022-03-18 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VictoryApp', '0006_auto_20220316_2338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'C. Categorías'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'D. Productos'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='producto',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='VictoryApp.Category', verbose_name='Tipo'),
            preserve_default=False,
        ),
    ]
