from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter

# Register your models here.
from .models import Alumno


admin.site.site_header = 'Administración de alumnos de La pileta de Liliana'
admin.site.site_title = 'Administración de alumnos'
admin.site.index_title = 'Benvenido al portal de administración de alumnos de La pileta de Liliana'

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'telefono', 'horario','cl1', 'cl2', 'cl3','cl4','cl5','cl6','cl7','cl8','cl9','cl10' ,'deuda', 'pagado', 'desc_familia')
    list_display_links = ('nombre', 'apellido', 'horario')
    list_editable = ('pagado',  'cl1', 'cl2', 'cl3','cl4','cl5','cl6','cl7','cl8','cl9','cl10')
    search_fields = ('nombre', 'apellido','horario')
    # list_filter = ('actividad', 'pagado', 'cargado', 'discapacidad', 'desc_familia')


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





