from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Empleado, Tarea, Proyecto
from .forms import EmpleadoForm, TareaForm, ProyectoForm
from django.views.generic import  DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse


def index(request):
    return HttpResponse("Listado de departamentos")

#Encargada de mostrar toda la lista de empleados, ordenados por id
def pruebalista(request):
    empleados =Empleado.objects.order_by('id')
    context = {'lista_empleado': empleados,
               'titulo_pagina':'Listado de empleados',
               'titulo_pagina1':'Empleados'}
    return render(request, 'lista_empleados.html', context)

#Encargado de mostrar un único empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        context['titulo_pagina1'] = 'Detalles del empleado'
        print(context)
        return context

#Las siguientes dos funciones se encargan de crear el formulario y de la creaciónd de el empleado
def show_form(request):
    return render(request, 'crear_empleado.html')

def crearempleado(request):
    nombre = request.POST["nombre"]
    apellido = request.POST["apellido"]
    dni = request.POST["dni"]
    telefono = request.POST["telefono"]
    email = request.POST["email"]
    empleado = Empleado()
    empleado.dni = dni
    empleado.nombre = nombre
    empleado.apellido= apellido
    empleado.email = email
    empleado.telefono = telefono
    empleado.save()
    return redirect('listaempleados')

#Encargado de la eliminación de el empleado seleccionado
class EmpleadosDeleteView(DeleteView):
    model = Empleado
    template_name = 'eliminar_empleado.html'
    success_url = reverse_lazy('listaempleados')

#Encargada de actualizar el empleado seleccionado
class EmpleadosUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'modificar_empleado.html'
    success_url = reverse_lazy('listaempleados')

#Encargado de mostrar un único empleado
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'
    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        context['titulo_pagina1'] = 'Detalles de la tarea'
        print(context)
        return context
#Encargada de mostrar toda la lista de tareas, ordenadas por id
def pruebalistatarea(request):
    tareas =Tarea.objects.order_by('id')
    context = {'lista_tareas': tareas,
               'titulo_pagina':'Listado de tareas'}
    return render(request, 'lista_tareas.html', context)

#Encargada de mostrar una tarea
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'
    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        return context

#Encargada de la creacion de tareas
def showform_proy1(request):
    listaempleados = Empleado.objects.order_by('id')
    context = {'listaempleados': listaempleados}
    context['titulo_pagina'] = 'Crear tarea'
    context['titulo_pagina1'] = 'Crear tarea'
    return render(request, 'crear_tarea.html', context)

def creartarea(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    inicio = request.POST["inicio"]
    fin = request.POST["fin"]
    responsable = request.POST["responsable"]
    prioridad = request.POST["prioridad"]
    estado = request.POST["estado"]
    notas = request.POST["notas"]
    tarea = Tarea()
    tarea.nombre = nombre
    tarea.descripcion = descripcion
    tarea.inicio = inicio
    tarea.fin = fin
    tarea.responsable = responsable
    tarea.prioridad = prioridad
    tarea.estado = estado
    tarea.notas = notas
    tarea.save()
    listaempleados = request.POST.getlist("responsable")
    for id in listaempleados:
        empleado = Empleado.objects.get(pk=id)
        tarea.responsable.add(empleado)
    tarea.save()
    return redirect('listatareas')

#Encargado de la eliminación de una tarea
def eliminar_tarea(request,id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method =="POST":
        tarea.delete()
        return redirect()
    context={
        "object":tarea
    }
    context['titulo_pagina'] = 'Eliminación de tarea'
    context['titulo_pagina1'] = 'Eliminar tarea'
    return render(request,"eliminar_tarea.html", context)



#Encargada de mostrar toda la lista de proyectos, ordenados por inicio
def pruebalistaproyecto(request):
    proyectos =Proyecto.objects.order_by('id')
    context = {'lista_proyectos': proyectos,
               'titulo_pagina':'Gestor de proyectos',
               'titulo_pagina1':'Gestion de proyectos'}
    return render(request, 'lista_proyectos.html', context)

#Encargada de mostrar un proyecto
class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'
    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        context['titulo_pagina1'] = 'Detalles del proyecto'
        return context

#Encargada de la creacion de proyectos
def showform_proy(request):
    listaempleados = Empleado.objects.order_by('id')
    context = {'listaempleados': listaempleados}
    context['titulo_pagina'] = 'Crear proyecto'
    context['titulo_pagina1'] = 'Crear proyecto'
    return render(request, 'crear_proyecto.html', context)


def crearproyecto(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    inicio = request.POST["inicio"]
    fin = request.POST["fin"]
    presupuesto = request.POST['presupuesto']
    cliente = request.POST['cliente']
    proyecto = Proyecto()
    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.inicio = inicio
    proyecto.fin = fin
    proyecto.presupuesto = presupuesto
    proyecto.cliente = cliente
    proyecto.save()
    Listaempleados = request.POST.getlist("empleados")
    for cosa in Listaempleados:
        empleado = Empleado.objects.get(pk=cosa)
        proyecto.empleados.add(empleado)
    proyecto.save()
    return redirect('listaproyectos')

class ProyectosDeleteView(DeleteView):
    model = Proyecto
    template_name = 'eliminar_proyecto.html'
    success_url = reverse_lazy('listaproyectos')


class ProyectosUpdateView(UpdateView):
    model = Proyecto
    fields = '__all__'
    listaempleados = Empleado.objects.order_by('id')
    context = {'listaempleados': listaempleados}
    template_name = 'modificar_proyecto.html'
    success_url = reverse_lazy('listaproyectos')
