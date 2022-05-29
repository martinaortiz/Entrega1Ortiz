
from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    nombre = models.CharField(max_length=30)
    division =  models.CharField(max_length=2)
    deporte =  models.CharField(max_length=30)
   
class Jugadora(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(default='')
    club = models.CharField(max_length=30)

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

