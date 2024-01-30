from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('carrera/', views.carrera, name='carrera'),
    path('guardarCarrera/', views.guardarCarrera),
    path('eliminarCarrera/<idCarreraJTVE>', views.eliminarCarrera),
    path('editarCarrera/<idCarreraJTVE>', views.editarCarrera),
    path('procesarinformacionCarrera/', views.procesarinformacionCarrera),
    path('curso/', views.curso, name='curso'),
    path('guardarCurso/', views.guardarCurso),
    path('eliminarCurso/<idCursoJTVE>', views.eliminarCurso),
    path('editarCurso/<idCursoJTVE>', views.editarCurso),
    path('procesarinformacionCurso/', views.procesarinformacionCurso),
    path('asignatura/', views.asignatura, name='asignatura'),
    path('guardarAsignatura/', views.guardarAsignatura),
    path('eliminarAsignatura/<idAsignaturaJTVE>', views.eliminarAsignatura),
    path('editarAsignatura/<idAsignaturaJTVE>', views.editarAsignatura),
    path('procesarinformacionAsignatura/', views.procesarinformacionAsignatura),

]
