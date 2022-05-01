
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from django.shortcuts import render
from django.template import Template
from AppCoder.forms import CursoFormulario, MiEstudiante, Profesores
from AppCoder.models import Estudiante

def curso(request):

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


    return render(request, 'AppCoder/curso.html', {'miFormulario':miFormulario})



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
    