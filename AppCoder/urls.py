from django.urls import path
from AppCoder import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('clubes', views.club, name='Clubes'),
    path('jugadora', views.jugadora, name='Jugadoras'),
    path('torneo', views.torneo, name='Torneo'),
    path('buscar/', views.buscar),

    path('club/lista', views.ClubList.as_view(), name='ListClubes'),
    path(r'^(?P<pk>\d+)$', views.ClubDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClubCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ClubUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ClubDelete.as_view(), name='Delete'),

    #path('jugadora/lista', views.JugadoraList.as_view(), name='ListJugadora'),
    #path(r'^(?P<pk>\d+)$', views.JugadoraDetalle.as_view(), name='DetailJugadora'),
    #path(r'^nuevo$', views.JugadoraCreacion.as_view(), name='NewJugadora'),
    #path(r'^editar/(?P<pk>\d+)$', views.JugadoraUpdate.as_view(), name='EditJugadora'),
    #path(r'^borrar/(?P<pk>\d+)$', views.JugadoraDelete.as_view(), name='DeleteJugadora'),
    

    path('login', views.login_request, name='Login'),
    path('register', views.register, name= 'Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarUsuario', views.editarUsuario, name='EditarUsuario'),
    

    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)