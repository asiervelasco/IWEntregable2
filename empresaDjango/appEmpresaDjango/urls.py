from django.urls import path
from . import views

urlpatterns = [
     path('empleado/lista/', views.pruebalista, name='listaempleados'),
     path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleadoun'),
     path('empleado/creacion/', views.show_form, name='creador_empleado'),
     path('empleado/crear/', views.crearempleado, name='crear_empleado'),
     path('empleado/<int:id>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),

     path('tarea/lista/', views.pruebalistatarea, name='listatareas'),
     path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tareaun'),
     path('tarea/crear/', views.creartarea, name='crear_tarea'),
     path('tarea/creacion/', views.show_form1, name='creador_tarea'),
     path('tarea/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),

     path('proyecto/lista/', views.pruebalistaproyecto, name='listaproyectos'),
     path('proyecto/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyectoun'),
     path('proyecto/crear/', views.CrearProyecto.as_view(), name='crear_proyecto'),
     path('proyecto/creacion/', views.show_form, name='creador_proyecto'),
     path('proyecto/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
]