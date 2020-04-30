from django.urls import path
from . import views

urlpatterns = [
     path('empleado/lista/', views.pruebalista, name='listaempleados'),
     path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleadoun'),
     path('empleado/creacion/', views.show_form, name='creador_empleado'),
     path('empleado/crear/', views.crearempleado, name='crear_empleado'),
     path('empleado/actualizar/<int:pk>', views.EmpleadosUpdateView.as_view(), name='empleadosUpdateView'),
     path('empleado/borrar/<int:pk>', views.EmpleadosDeleteView.as_view(), name='empleadosDeleteView'),

     path('tarea/lista/', views.pruebalistatarea, name='listatareas'),
     path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tareaun'),
     path('tarea/crear/', views.creartarea, name='crear_tarea'),
     path('tarea/creacion/', views.showform_proy1, name='creador_tarea'),
     path('tarea/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),

     path('proyecto/lista/', views.pruebalistaproyecto, name='listaproyectos'),
     path('proyecto/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyectoun'),
     path('proyecto/creacion/', views.showform_proy, name='creador_proyecto'),
     path('proyecto/crear/', views.crearproyecto, name='crear_proyecto'),
     path('proyecto/<int:pk>/eliminar/', views.ProyectosDeleteView.as_view(), name='eliminar_proyecto'),
     path('proyecto/<int:pk>/actualizar/', views.ProyectosUpdateView.as_view(), name='actualizar_proyecto'),

]