
from django.db import models


class Club(models.Model):
    nombre = models.CharField(max_length=30)
    division =  models.CharField(max_length=2)
    deporte =  models.CharField(max_length=30)
   
class Jugadora(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(default='')
    club = models.CharField(max_length=30)
    deporte = models.CharField(max_length=30)

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    materia = models.CharField(max_length=30)
    mail = models.EmailField()
    class Meta:
        verbose_name='Profesor'
        verbose_name_plural = 'Profesores'

