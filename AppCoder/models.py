
from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    division =  models.CharField(max_length=2)
    deporte =  models.CharField(max_length=30)
   
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

