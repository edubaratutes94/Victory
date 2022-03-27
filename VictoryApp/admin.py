from django.contrib import admin
from VictoryApp.models import *
# Register your models here.


class AdminEntity(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    list_filter = ["name"]
    class Meta:
        model = Entity
admin.site.register(Entity,AdminEntity)

class AdminBlog(admin.ModelAdmin):
    list_display = ["id", "title", 'active']
    list_display_links = ["id", "title"]
    list_filter = ["title"]
    list_editable = ["active"]
    list_per_page = 10
    class Meta:
        model = Blog
admin.site.register(Blog,AdminBlog)

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ["id", "name"]
    list_filter = ['name']
    list_per_page = 10

    class Meta:
        model = Category
admin.site.register(Category, AdminCategory)

class AdminProduct(admin.ModelAdmin):
    list_display = ["id", "name", 'active']
    list_display_links = ["id", "name"]
    list_filter = ["name"]
    list_editable = ["active"]
    list_per_page = 10
    class Meta:
        model = Product
admin.site.register(Product,AdminProduct)

class ProductGaleryAdmin(admin.ModelAdmin):
    list_display = ['smallDesc']
    list_display_links = ["smallDesc"]
    list_filter = ['producto']
    list_per_page = 10

    class Meta:
        model = ProductGalery
admin.site.register(ProductGalery, ProductGaleryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_display_links = ["name", 'email']
    list_filter = ['email']
    list_per_page = 10

    class Meta:
        model = Comment
admin.site.register(Comment, CommentAdmin)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'fecha_hora', 'cant_persona', 'phone','active']
    list_display_links = ["full_name", 'phone']
    list_filter = ['phone', 'full_name']
    list_editable = ['active']
    list_per_page = 10

    class Meta:
        model = Reservation
admin.site.register(Reservation, ReservaAdmin)
