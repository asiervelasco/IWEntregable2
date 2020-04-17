from django.contrib import admin
from .models import Empleado, Tarea, Proyecto

admin.site.register(Empleado)
admin.site.register(Tarea)
admin.site.register(Proyecto)

