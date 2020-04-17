from django.urls import path
from . import views

urlpatterns = [
     path('empleado/', views.EmpleadoListView.as_view(), name='lista_empleados'),
     path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado'),
]