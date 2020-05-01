from django.contrib import admin
from .models import Empleado, Tarea, Proyecto, Cliente

admin.site.register(Empleado)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Cliente)

