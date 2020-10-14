from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

# Register your models here.
from .models import Alumno
from .models import Alumno_mes



admin.site.site_header = 'Administración de alumnos de La pileta de Liliana'
admin.site.site_title = 'Administración de alumnos'
admin.site.index_title = 'Benvenido al portal de administración de alumnos de La pileta de Liliana'

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido','horario', 'edad', 'telefono', 'email', 'desc_familia','deuda','discapacidad', 'comentarios')
    list_display_links = ('nombre', 'apellido')
    list_editable = ('horario', 'telefono', 'email', 'deuda')
    search_fields = ('nombre', 'apellido','horario')




@admin.register(Alumno_mes)
class Alumno_mesAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'horario','cl1', 'cl2', 'cl3','cl4','cl5','cl6','cl7','cl8','cl9','cl10' ,'deuda', 'fecha_pago', 'desc_familia')
    list_display_links = ('nombre', 'apellido', 'horario')
    list_editable = (  'cl1', 'cl2', 'cl3','cl4','cl5','cl6','cl7','cl8','cl9','cl10', 'deuda', 'fecha_pago')
    search_fields = ('nombre', 'apellido','horario')



