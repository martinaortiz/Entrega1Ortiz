from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ClubFormulario(forms.Form):

    club = forms.CharField()
    division = forms.CharField()
    deporte = forms.CharField()

class JugadoraForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    mail = forms.EmailField()
    club = forms.CharField()
    deporte = forms.CharField()



class Profesores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    materia = forms.CharField()
    mail = forms.EmailField()


class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 