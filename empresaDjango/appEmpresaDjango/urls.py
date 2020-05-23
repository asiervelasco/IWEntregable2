from django.urls import path
from . import views

#Listado de urls para la navegación del proyecto

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
     path('tarea/<int:pk>/eliminar/', views.TareaDeleteView.as_view(), name='eliminar_tarea'),
     path('tarea/<int:pk>/actualizar/', views.TareaUpdateView.as_view(), name='actualizar_tarea'),

     path('proyecto/lista/', views.pruebalistaproyecto, name='listaproyectos'),
     path('proyecto/<int:id>/', views.proyectodetalles, name='proyectoun'),
     path('proyecto/creacion/', views.showform_proy, name='creador_proyecto'),
     path('proyecto/crear/', views.crearproyecto, name='crear_proyecto'),
     path('proyecto/<int:pk>/eliminar/', views.ProyectosDeleteView.as_view(), name='eliminar_proyecto'),
     path('proyecto/<int:pk>/actualizar/', views.ProyectosUpdateView.as_view(), name='actualizar_proyecto'),

     path('cliente/lista/', views.pruebalistaclientes, name='listaclientes'),
     path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),
     path('cliente/creacion/', views.show_formC, name='creador_cliente'),
     path('cliente/crear/', views.crearCliente, name='crear_cliente'),
     path('cliente/actualizar/<int:pk>', views.ClienteUpdateView.as_view(), name='clienteUpdateView'),
     path('cliente/borrar/<int:pk>', views.ClienteDeleteView.as_view(), name='clienteDeleteView'),

     path('email/',views.devolvermail, name='email'),

     path('clientes/', views.ClientesCreación.as_view(), name='clientescrear'),
     path('marcarTarea/', views.marcartareacomoFinalizada, name='marcar_tarea')
]