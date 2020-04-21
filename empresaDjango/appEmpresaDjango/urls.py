from django.urls import path
from . import views

urlpatterns = [
     path('empleado/lista/', views.EmpleadoListView.as_view(), name='lista_empleados'),
     path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
     path('empleado/crear/', views.CrearEmpleado.as_view(), name='crear_empleado'),
     path('tarea/lista/', views.TareaListView.as_view(), name='lista_tareas'),
     path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='tarea'),
     path('tarea/crear/', views.CrearTarea.as_view(), name='crear_tarea')
]