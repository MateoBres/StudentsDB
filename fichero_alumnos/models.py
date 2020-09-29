from django.db import models
from datetime import datetime

# Create your models here.
class Alumno(models.Model):
    deuda = models.CharField(max_length=30, blank=True, null=True, default='')
    pagado = models.BooleanField()

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, blank=True, null=True, default='')
    edad = models.IntegerField(blank=True, null=True, default='')
    familiar_nombre = models.CharField(max_length=30, blank=True, null=True, default='')

    telefono = models.CharField(max_length=30, blank=True, null=True, default='')
    email = models.EmailField(blank=True, null=True, default='')

    nacimiento = models.CharField(help_text='01/01/2001', max_length=30, blank=True, null=True)    
    cargado = models.DateField(auto_now_add=True)
    desc_familia = models.BooleanField()
    discapacidad = models.BooleanField()
    comentarios = models.TextField(blank=True, null=True)
    VECES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        )
    veces = models.IntegerField(choices=VECES, default='')
    dias = models.CharField(max_length=30,blank=True, null=True, default='')
    horario = models.CharField(max_length=30,blank=True, null=True, default='')
    ACTIVIDAD = (
        ('Bebes','Bebes'),
        ('Escuelita','Escuelita'),
        ('AquaGym','AquaGym'),
        ('AquaFitness','AquaFitness'),
    )
    actividad = models.CharField(max_length=30,choices=ACTIVIDAD, default='')
    
    foto = models.ImageField(upload_to='fotos/alumnos', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self): 
        return self.nombre