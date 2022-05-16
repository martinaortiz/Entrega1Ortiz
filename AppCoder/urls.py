from django.urls import path
from AppCoder import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('clubes', views.club, name='Clubes'),
    path('estudiante', views.estudiante, name='Estudiantes'),
    path('profesor', views.profesor, name='Profesores'),
    #path('busquedaCamada', views.busquedaCamada, name= 'BusquedaCamada'),
    path('buscar/', views.buscar),

    path('club/lista', views.ClubList.as_view(), name='ListClubes'),
    path(r'^(?P<pk>\d+)$', views.ClubDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClubCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ClubUpdate.as_view(), name='Edit'),
    path(r'^borrar(?P<pk>\d+)$', views.ClubDelete.as_view(), name='Delete'),
    
    path('login', views.login_request, name='Login'),
    #path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='logout'),

    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)