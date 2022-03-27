from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Entity(models.Model):
    created_at = models.DateTimeField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slogan_1 = models.CharField(max_length=255, verbose_name="Slogan nivel 1", blank=True, null=True)
    slogan_2 = models.CharField(max_length=255, verbose_name="Slogan nivel 2", blank=True, null=True)
    slogan_3 = models.CharField(max_length=255, verbose_name="Slogan nivel 3", blank=True, null=True)
    descripcion_contact=RichTextField(verbose_name="Descripcion de contacto")
    image_banner_1 = models.ImageField(upload_to='static/upload', verbose_name="Imagen Banner Inicio")
    image_banner_2 = models.ImageField(upload_to='static/upload', verbose_name="Imagen Banner Header")
    image_left = models.ImageField(upload_to='static/upload', verbose_name="Imagen Izquierda")
    image_right = models.ImageField(upload_to='static/upload', verbose_name="Imagen Derecha")
    image_deep = models.ImageField(upload_to='static/upload', verbose_name="Imagen Fondo Reservar")
    image_small = models.ImageField(upload_to='static/upload', verbose_name="Imagen Reservar")
    image_prefooter = models.ImageField(upload_to='static/upload', verbose_name="Imagen PreFooter")
    address = models.CharField(max_length=255, verbose_name="Direccion", blank=True, null=True)
    email = models.EmailField(verbose_name="Correo", blank=True, null=True)
    map_addres = models.URLField(verbose_name="Direccion google maps, src")
    phone = models.CharField(max_length=255, verbose_name="Telefono")
    face = models.URLField(verbose_name="Facebook",  blank=True, null=True)
    inst = models.URLField(verbose_name="Instagram", blank=True, null=True)
    twit = models.URLField(verbose_name="Twitter",  blank=True, null=True)
    yout = models.URLField(verbose_name="YouTube", blank=True, null=True)
    link = models.URLField(verbose_name="Linkedin", blank=True, null=True)

    class Meta:
        verbose_name_plural = "A. Entidad"

    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    title = models.CharField(max_length=255, verbose_name="Título")
    text_autor = models.CharField(max_length=255, verbose_name="Datos del Autor", blank=True, null=True)
    descripcion = RichTextField(verbose_name="Descripción")
    active = models.BooleanField(verbose_name="Activado", default=False)
    image = models.ImageField(upload_to="static/upload", verbose_name="Imagen", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "B. Blog"

class Category(models.Model):
    created_at = models.DateTimeField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image = models.ImageField(upload_to='static/upload', verbose_name="Imagen Categoria")
    descripcion = RichTextField(verbose_name="Descripcion", default='')

    class Meta:
        verbose_name_plural = "C. Categorías"

    def __str__(self):
        return str(self.name)

class Product(models.Model):
    created_at = models.DateField(verbose_name="Creado", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image = models.ImageField(upload_to='static/upload', verbose_name="Imagen Producto")
    category = models.ForeignKey(Category, models.PROTECT, verbose_name="Tipo")
    active = models.BooleanField(verbose_name="Activado", default=False)
    descripcion = RichTextField(verbose_name="Descripcion", default='')
    price = models.FloatField(default=0, verbose_name="Precio del servicio")

    class Meta:
        verbose_name_plural = "D. Productos"

    def __str__(self):
        return str(self.name)

class ProductGalery(models.Model):
    image = models.ImageField(upload_to='static/upload', verbose_name="Imagen")
    producto = models.ForeignKey(Product, verbose_name="Servicio", on_delete=models.PROTECT)
    smallDesc = models.CharField(max_length=255, verbose_name="Pequeña descripcion", null=True, blank=True)
    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name_plural = "E. Galería del Producto"

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Telefono", default='')
    text = models.TextField(verbose_name="Mensaje")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "F. Comentarios del Sitio"

class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")
    fecha_hora = models.DateTimeField(max_length=255,verbose_name="Fecha de la reservación")
    email = models.EmailField(max_length=255,verbose_name="Email")
    phone = models.CharField(max_length=255, verbose_name="Telefono", default='')
    full_name= models.CharField(max_length=255, verbose_name="Nombre Completo")
    cant_persona = models.IntegerField(verbose_name="Cantidad de Personas")
    active = models.BooleanField(verbose_name="Activado", default=False)
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "G. Reservaciones"
        ordering = ['fecha_hora']
