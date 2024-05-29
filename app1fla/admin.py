from django.contrib import admin

# Register your models here.
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
