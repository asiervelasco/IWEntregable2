from django.urls import path
from . import views

urlpatterns = [
     path('empleado/lista/', views.pruebalista, name='listaempleados'),
     path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleadoun'),
     path('empleado/crear/', views.CrearEmpleado.as_view(), name='crear_empleado'),
     path('empleado/modificar/<int:pk>/', views.modificarEmpleado.as_view(), name='modificar_empleado'),
     path('tarea/lista/', views.pruebalistatarea, name='listatareas'),
     path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tareaun'),
     path('tarea/crear/', views.CrearTarea.as_view(), name='crear_tarea'),
     path('proyecto/lista/', views.pruebalistaproyecto, name='listaproyectos'),
     path('proyecto/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyectoun'),
     path('proyecto/crear/', views.CrearProyecto.as_view(), name='crear_proyecto'),
]