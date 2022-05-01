from django.urls import path
from AppCoder import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('cursos', views.curso, name='Cursos'),
    path('estudiante', views.estudiante, name='Estudiantes'),
    path('profesor', views.profesor, name='Profesores'),
    #path('busquedaCamada', views.busquedaCamada, name= 'BusquedaCamada'),
    path('buscar/', views.buscar),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)