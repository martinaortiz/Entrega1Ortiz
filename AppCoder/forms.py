
from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()
    duracion = forms.IntegerField()

class MiEstudiante(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()



class Profesores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    materia = forms.CharField()
    mail = forms.EmailField()