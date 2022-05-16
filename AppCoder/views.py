
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from django.shortcuts import render
from django.template import Template
from AppCoder.forms import CursoFormulario, MiEstudiante, Profesores
from AppCoder.models import Estudiante
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

@login_required
def club(request):

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST) #aca llega la info del formulario

        print(miFormulario) #muestra en terminal

        if miFormulario.is_valid():        #comprobar si la info es valida

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'], duracion=informacion['duracion']) #creo el curso con la info recivida

            curso.save()

            return render(request, 'AppCoder/inicio.html') #una vez guardado mostramos la plantilla de inicio

    else:
        miFormulario = CursoFormulario() #me muestra un formulario vacio


    return render(request, 'AppCoder/cursos/curso.html', {'miFormulario':miFormulario})

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'AppCoder/cursos/cursos_list.html'

class CursoDetalle(DetailView):
    model = Curso
    template_name= 'AppCoder/cursos/curso_detalle.html'

class CursoCreacion(CreateView):
    model = Curso
    success_url= '/AppCoder/curso/lista'
    fields= ['nombre', 'camada', 'duracion']

class CursoUpdate(UpdateView):
    model = Curso
    success_url= '/AppCoder/curso/lista'
    fields= ['nombre', 'camada', 'duracion']

class CursoDelete(DeleteView):
    model = Curso
    success_url= 'AppCoder/curso/lista'


def estudiante(request):
  
     if request.method == 'POST':

        miEstudiante = MiEstudiante(request.POST) 

        print(miEstudiante) 

        if miEstudiante.is_valid():        

            info1 = miEstudiante.cleaned_data

            estudiante = Estudiante(nombre=info1['nombre'], apellido=info1['apellido'], mail=info1['mail'])  

            estudiante.save()

            return render(request, 'AppCoder/inicio.html') 

     else:
        miEstudiante = MiEstudiante() 


     return render(request, 'AppCoder/estudiante.html', {'miEstudiante': miEstudiante})
    




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

    if request.GET['camada']:

        camada= request.GET['camada']
        #curso = Curso.objects.filter(camada__icontains=camada) #icontains significa que el numero que buscamos esta dentro del numero de camada
        curso = Curso.objects.filter(camada__iexact=camada)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'curso':curso, 'camada':camada})

    else:
        respuesta= 'No enviaste datos'

    return HttpResponse(respuesta)
    