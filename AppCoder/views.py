
from django.http import HttpResponse
from AppCoder.models import Club, Jugadora, Profesor
from django.shortcuts import render
from django.template import Template
from AppCoder.forms import ClubFormulario, JugadoraForm, Profesores, RegistroFormulario
from AppCoder.models import Jugadora
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
    
        form = RegistroFormulario(request.POST) #LEER LA DATA DEL FORMULARIO DE INICIO DE SESION

        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()

            return render(request, 'AppCoder/inicio.html', {'mensaje':'Usuario Creado'})
    else:
        form = RegistroFormulario()
    
    return render(request, 'AppCoder/registro.html', {'form': form})



def login_request(request):

    if request.method == 'POST': #al presionar el boton iniciar sesion
        
        form = AuthenticationForm(request, data=request.POST) #LEER LA DATA DEL FORMULARIO DE INICIO DE SESION

        if form.is_valid():

            usuario= form.cleaned_data.get('username') #leer el usuario ingresado
            contra= form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra) #buscar al usuario con los datos ingresados

            if user:  #si ha encontrado un usuario con esos datos

                login(request, user) #hacemos login
                #mostramos la pg de inicio con un mensaje de bienvenida
                return render(request, 'AppCoder/inicio.html', {'mensaje':f"Bienvenido {user}"})
            
        else: # si el formulario no es valido(no encuentra el usuario)
                #mostramos la pag de inicio junto a un mensaje de error
            return render(request, 'AppCoder/inicio.html', {'mensaje':"Error. Datos incorrectos"})
    
    else:
        
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "AppCoder/login.html", {'form':form}) #vincular la vista con la plantilla de html


def club(request):

    if request.method == 'POST':

        miFormulario = ClubFormulario(request.POST) #aca llega la info del formulario

        print(miFormulario) #muestra en terminal

        if miFormulario.is_valid():        #comprobar si la info es valida

            informacion = miFormulario.cleaned_data

            club = Club(nombre=informacion['club'], division=informacion['division'], deporte=informacion['deporte']) #creo el curso con la info recivida

            club.save()

            return render(request, 'AppCoder/inicio.html') #una vez guardado mostramos la plantilla de inicio

    else:
        miFormulario = ClubFormulario()  #me muestra un formulario vacio


    return render(request, 'AppCoder/clubes/club.html', {'miFormulario':miFormulario})

class ClubList(LoginRequiredMixin, ListView):
    model = Club
    template_name = 'AppCoder/clubes/clubes_list.html'

class ClubDetalle(DetailView):
    model = Club
    template_name= 'AppCoder/clubes/club_detalle.html'

class ClubCreacion(CreateView):
    model = Club
    success_url= '/AppCoder/club/lista'
    fields= ['nombre', 'division', 'deporte']

class ClubUpdate(UpdateView):
    model = Club
    success_url= '/AppCoder/club/lista'
    fields= ['nombre', 'division', 'deporte']

class ClubDelete(DeleteView):
    model = Club
    success_url= '/AppCoder/club/lista'


def jugadora(request):
  
     if request.method == 'POST':

        miFormulario = JugadoraForm(request.POST) 

        print(miFormulario) 

        if miFormulario.is_valid():        

            info1 = miFormulario.cleaned_data

            jugadora = Jugadora(nombre=info1['nombre'], apellido=info1['apellido'], mail=info1['mail'], club=info1['club'], deporte=info1['deporte'])  

            jugadora.save()

            return render(request, 'AppCoder/inicio.html') 

     else:
        miFormulario = JugadoraForm() 


     return render(request, 'AppCoder/jugadoras/jugadora.html', {'miFormulario': miFormulario})


class JugadoraList(LoginRequiredMixin, ListView):
    model = Jugadora
    template_name = 'AppCoder/jugadoras/jugadora_list.html'

class JugadoraDetalle(DetailView):
    model = Jugadora
    template_name= 'AppCoder/jugadoras/jugadora_detalle.html'

class JugadoraCreacion(CreateView):
    model = Jugadora
    success_url= '/AppCoder/jugadora/lista'
    fields= ['nombre', 'apellido', 'mail', 'club', 'deporte']

class JugadoraUpdate(UpdateView):
    model = Jugadora
    success_url= '/AppCoder/jugadora/lista'
    fields= ['nombre', 'apellido', 'mail', 'club', 'deporte']

class JugadoraDelete(DeleteView):
    model = Jugadora
    success_url= '/AppCoder/jugadora/lista'






def profesor(request):
  
     if request.method == 'POST':

        profesores = Profesores(request.POST) 

        print(profesores) 

        if profesores.is_valid():       

            info2 = profesores.cleaned_data

            profesor = Profesor(nombre=info2['nombre'], apellido=info2['apellido'], materia=info2['materia'], mail=info2['mail']) #creo el curso con la info recivida

            profesor.save()

            return render(request, 'AppCoder/inicio.html') 

     else:
        profesores = Profesores() 


     return render(request, 'AppCoder/profesor.html', {'profesores': profesores})


def inicio(request):

    return render(request, 'AppCoder/inicio.html')


#def busquedaCamada(request):

  #  return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):

    if request.GET['deporte']:

        deporte= request.GET['deporte']
        #curso = Curso.objects.filter(camada__icontains=camada) #icontains significa que el numero que buscamos esta dentro del numero de camada
        club = Club.objects.filter(deporte__iexact=deporte)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'club':club, 'deporte':deporte})

    else:
        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)
    