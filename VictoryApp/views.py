from unicodedata import category
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from VictoryApp import models
from Victory import settings
import sweetify
from django.template.loader import render_to_string
from datetime import datetime
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
# Create your views here.

# Funcion para la vista Inicio
def home(request):
    if request.POST:
        name = request.POST.get('name', None)
        persons = request.POST.get('persons', None)
        datetimes = request.POST.get('datetimes', None)
        email = request.POST.get('email', None)
        phone = request.POST.get('phone', None)
        reservacion = models.Reservation.objects.create(full_name=name, email=email, cant_persona=persons,
                                                        fecha_hora=datetimes,
                                                        phone=phone)
        reservacion.save()
        fecha = datetime.strptime(reservacion.fecha_hora, "%Y-%m-%dT%H:%M")
        subject = _('Nueva Reservación')
        message = render_to_string('correo.html', {
            'reserva': reservacion,
            'fecha': fecha,
        })
        users = models.User.objects.all()
        for user in users.all():
            x = user
            send_mail(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      [x.email]  # destinatarios
                      )
        sweetify.success(request, 'Reserva realizada con éxito', button='Ok', timer=5000)
        return HttpResponseRedirect('/')
    category = models.Category.objects.all()[:4]
    product = models.Product.objects.filter(active=True).all()[:3]
    blog = models.Blog.objects.filter(active=True).order_by("-id").all()[:6]
    return render(request, 'index.html', {'category': category, 'product': product, 'blog': blog})

# Funcion para la vista Contactos
def contact(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        comentario = models.Comment.objects.create(name=name, email=email, phone=phone, text=message)
        comentario.save()
        sweetify.success(request, 'Mensaje enviado con éxito', button='Ok', timer=5000)
        return HttpResponseRedirect("/contact/")
    return render(request, "contact.html")

# Funcion para el listado de blog
def blog_list(request, index):
    blog = models.Blog.objects.order_by("-id").all()
    paginator = Paginator(blog, 8, index)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})

# Funcion para la vista en detalles de los blog
def blog_detail(request, id):
    blog = models.Blog.objects.filter(id=id)
    return render(request, 'blog_detail.html',
                  {'blog': blog.get()})

# Funcion para el listado de menus
def menu_list(request):
    categorias = models.Category.objects.all()
    return render(request, 'menu.html', {'categoria': categorias})
