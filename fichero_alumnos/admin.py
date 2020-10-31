# Django
from django.contrib import admin

# Models
from .models import Alumno




admin.site.site_header = 'Administración de alumnos de La pileta de Liliana'
admin.site.site_title = 'Administración de alumnos'
admin.site.index_title = 'Benvenido al portal de administración de alumnos de La pileta de Liliana'



@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'horario','cl1', 'cl2', 'cl3','cl4','cl5','cl6','cl7','cl8','cl9','cl10' ,'deuda', 'fecha_pago', 'desc_familia')
    list_display_links = ('nombre', 'apellido', 'horario')
    list_editable = (  'cl1', 'cl2', 'cl3','cl4','cl5','cl6','cl7','cl8','cl9','cl10', 'deuda', 'fecha_pago')
    search_fields = ('nombre', 'apellido','horario')

    fieldsets = (
        ('Datos Personales', {
            'fields': (('nombre', 'apellido'),
                ('edad', 'familiar_nombre'),
                ('telefono', 'email'),
                ('nacimiento',))
        }),
        ('Turno', {
            'fields': (('horario', 'actividad'),
            ('deuda', 'desc_familia'),
            )
        }),
         ('Clases', {
            'fields': (('cl1', 'cl2'), ('cl3', 'cl4'), ('cl5', 'cl6'), ('cl7', 'cl8'), ('cl9', 'cl10'),)
        }),
        ('Información extra', {
            'fields': (('discapacidad', 'comentarios'),
            ('foto', 'fecha_pago'))
        }),
    )

