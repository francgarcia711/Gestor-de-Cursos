from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    
    #inicio
    path('inicio/', views.inicio, name='inicio'),
    
    # Estudiantes
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    
    # Profesores
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesorFormulario/', views.profesorFormulario, name='profesorFormulario'),
    path('profesor/editar/<int:id>/', views.profesor_editar, name='profesorEditar'),
    path('profesor/eliminar/<int:id>/', views.profesor_eliminar, name='profesorEliminar'),
    
    # Entregables
    path('entregables/', views.lista_entregables, name='lista_entregables'),
    
    # Cursos
    path('cursos/', views.cursos, name='cursos'),
    path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    
    #Buscador
    path('buscar/', views.buscar, name='buscar'),
    path('profesores/buscar/', views.buscar_profesor, name='buscar_profesor'),
]