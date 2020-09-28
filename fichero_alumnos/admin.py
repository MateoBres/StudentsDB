from django.contrib import admin

# Register your models here.
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'dias', 'horario', 'telefono', 'pagado')
    list_display_links = ('nombre', 'apellido', 'edad', 'dias', 'horario', 'telefono')
    list_editable = ('pagado',)
    search_fields = ('nombre', 'apellido', 'dias', 'horario', 'telefono')
    list_filter = ('dias', 'edad', 'horario', 'pagado', 'deuda', 'cargado', 'discapacidad', 'desc_familia')