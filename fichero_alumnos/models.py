# Django
from django.db import models


#MODELO QUE NO TENES QUE TOCAR!!!

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True, default='')
    edad = models.IntegerField(blank=True, null=True, default='')
    familiar_nombre = models.CharField(max_length=30, blank=True, null=True, default='')

    telefono = models.CharField(help_text='0000  012345', max_length=30, blank=True, null=True, default='')
    email = models.EmailField(blank=True, null=True, default='')

    nacimiento = models.CharField(help_text='01/01/2001', max_length=30, blank=True, null=True)    
    cargado = models.DateField(auto_now_add=True)
    desc_familia = models.BooleanField()
    discapacidad = models.BooleanField()
    comentarios = models.TextField(blank=True, null=True)
   
    
    horario = models.CharField(help_text='00dia  /  00dia', max_length=30,blank=True, null=True, default='')
    ACTIVIDAD = (
        ('Bebes','Bebes'),
        ('Escuelita','Escuelita'),
        ('AquaGym','AquaGym'),
        ('AquaFitness','AquaFitness'),
    )
    actividad = models.CharField(max_length=30,choices=ACTIVIDAD, default='')
    deuda = models.CharField(max_length=20, blank=True, null=True, default='')
    fecha_pago = models.DateField(blank=True, null=True)
    cl1 = models.BooleanField()
    cl2 = models.BooleanField()
    cl3 = models.BooleanField()
    cl4 = models.BooleanField()
    cl5 = models.BooleanField()
    cl6 = models.BooleanField()
    cl7 = models.BooleanField()
    cl8 = models.BooleanField()
    cl9 = models.BooleanField()
    cl10 = models.BooleanField()
    
    foto = models.ImageField(upload_to='fotos/alumnos', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self): 
        return self.nombre


