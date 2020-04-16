from django.db import models
import datetime

class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.id} -> {self.dni}'

class Tarea(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=1000)
    inicio = models.DateField(default=datetime.date.today)
    fin = models.DateField(default=datetime.date.today)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    notas = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.id} -> {self.nombre}'

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=1000)
    inicio = models.DateField(default=datetime.date.today)
    fin = models.DateField(default=datetime.date.today)
    presupuesto = models.CharField(max_length=150)
    cliente = models.CharField(max_length=150)
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    empleados = models.ForeignKey(Empleado, on_delete=models.CASCADE)
