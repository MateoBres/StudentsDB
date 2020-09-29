from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

# Register your models here.
from .models import Alumno


admin.site.site_header = 'Administración de alumnos de La pileta de Liliana'
admin.site.site_title = 'Administración de alumnos'
admin.site.index_title = 'Benvenido al portal de administración de alumnos de La pileta de Liliana'

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'dias', 'horario', 'telefono', 'pagado','deuda')
    list_display_links = ('nombre', 'apellido', 'edad', 'dias', 'horario', 'telefono')
    list_editable = ('pagado','deuda')
    search_fields = ('nombre', 'apellido', 'dias', 'horario', 'telefono')
    list_filter = ('actividad', 'dias', 'edad', 'horario', 'pagado', 'deuda', 'cargado', 'discapacidad', 'desc_familia')


# class EdadFiltro(SimpleListFilter):
#     title ='Filtro Edad'
#     parameter_name = 'Edades'

#     def lookups(self, request, model_admin):
#         return (
#             ("value_01", "Value 01"),
#             ("maria", "Maria")
#         )
    
#     def queryset(self, request, queryset):
#         if self.value() == 'value_01':
#             queryset = queryset.order_by('nombre')

#         elif self.value() == 'maria':
#                 queryset = queryset.filter(nombre__contains='Maria')

#         return queryset





