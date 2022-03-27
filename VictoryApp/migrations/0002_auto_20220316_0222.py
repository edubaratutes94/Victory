# Generated by Django 3.0.1 on 2022-03-16 06:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VictoryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('text_autor', models.CharField(max_length=255, verbose_name='Datos del Autor')),
                ('descripcion', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('active', models.BooleanField(default=False, verbose_name='Activado')),
                ('image', models.ImageField(null=True, upload_to='static/upload', verbose_name='Imagen')),
            ],
            options={
                'verbose_name_plural': 'B. Blog',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='static/upload', verbose_name='Imagen Banner')),
                ('descripcion', ckeditor.fields.RichTextField(default='', verbose_name='Descripcion')),
            ],
            options={
                'verbose_name_plural': 'C. Categorías',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(default='', max_length=255, verbose_name='Telefono')),
                ('text', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name_plural': 'F. Comentarios del Sitio',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='static/upload', verbose_name='Imagen Banner')),
                ('active', models.BooleanField(default=False, verbose_name='Activado')),
                ('descripcion', ckeditor.fields.RichTextField(default='', verbose_name='Descripcion')),
                ('price', models.FloatField(default=0, verbose_name='Precio del servicio')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='VictoryApp.Category', verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'D. Productos',
            },
        ),
        migrations.RemoveField(
            model_name='entity',
            name='company_type',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='company_type_es',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='desc_es',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='image',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='slogan',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='slogan_es',
        ),
        migrations.AddField(
            model_name='entity',
            name='descripcion_contact',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Descripcion de contacto'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_banner_1',
            field=models.ImageField(default='static/frontend/img/banner-bg.jpg', upload_to='static/upload', verbose_name='Imagen Banner Inicio'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_banner_2',
            field=models.ImageField(default='static/frontend/img/heading-bg.jpg', upload_to='static/upload', verbose_name='Imagen Banner Header'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_deep',
            field=models.ImageField(default='static/frontend/img/book-bg.jpg', upload_to='static/upload', verbose_name='Imagen Fondo Reservar'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_left',
            field=models.ImageField(default='static/frontend/img/cook_01.jpg', upload_to='static/upload', verbose_name='Imagen Izquierda'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_prefooter',
            field=models.ImageField(default='static/frontend/img/signup-bg.jpg', upload_to='static/upload', verbose_name='Imagen PreFooter'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_right',
            field=models.ImageField(default='static/frontend/img/cook_02.jpg', upload_to='static/upload', verbose_name='Imagen Derecha'),
        ),
        migrations.AddField(
            model_name='entity',
            name='image_small',
            field=models.ImageField(default='static/frontend/img/book_left_image.jpg', upload_to='static/upload', verbose_name='Imagen Reservar'),
        ),
        migrations.AddField(
            model_name='entity',
            name='slogan_1',
            field=models.CharField(max_length=255, null=True, verbose_name='Slogan nivel 1'),
        ),
        migrations.AddField(
            model_name='entity',
            name='slogan_2',
            field=models.CharField(max_length=255, null=True, verbose_name='Slogan nivel 2'),
        ),
        migrations.AddField(
            model_name='entity',
            name='slogan_3',
            field=models.CharField(max_length=255, null=True, verbose_name='Slogan nivel 3'),
        ),
        migrations.CreateModel(
            name='ProductGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/upload', verbose_name='Imagen')),
                ('smallDesc_es', models.CharField(blank=True, max_length=255, null=True, verbose_name='Pequeña descripcion')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='VictoryApp.Product', verbose_name='Servicio')),
            ],
            options={
                'verbose_name_plural': 'E. Galería del Producto',
            },
        ),
    ]
