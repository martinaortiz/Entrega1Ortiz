
from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    duracion = models.IntegerField(default=0)
   
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(default='')

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    mail = models.EmailField()
    class Meta:
        verbose_name='Profesor'
        verbose_name_plural = 'Profesores'

