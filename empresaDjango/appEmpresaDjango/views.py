from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Empleado, Tarea, Proyecto
from .forms import EmpleadoForm, TareaForm, ProyectoForm
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404


def index(request):
    return HttpResponse("Listado de departamentos")
#Encargada de mostrar toda la lista de empleados, ordenados por id
def pruebalista(request):
    empleados =Empleado.objects.order_by('id')
    context = {'lista_empleado': empleados,
               'titulo_pagina':'Listado de empleados'}
    return render(request, 'lista_empleados.html', context)

#Encargado de mostrar un único empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        print(context)
        return context
#Encargado de la creación de un nuevo empleado
class CrearEmpleado(View):
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form' :  form,
            'titulo_pagina' : 'Crear nuevo empleado'
        }
        return render(request, 'crear_empleado.html', context)

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
        return render(request, 'crear_empleado.html', {'form': form, 'titulo_pagina': 'Crear nuevo empleado'})
#Encargada de mostrar toda la lista de tareas, ordenadas por inicio

def pruebalistatarea(request):
    tareas =Tarea.objects.order_by('id')
    context = {'lista_tareas': tareas,
               'titulo_pagina':'Listado de Tareas'}
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
class CrearTarea(View):
    def get(self, request, *args, **kwargs):
        form = TareaForm()
        context = {
            'form' :  form,
            'titulo_pagina' : 'Crear nueva tarea'
        }
        return render(request, 'crear_tarea.html', context)

    def post(self, request, *args, **kwargs):
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
        return render(request, 'crear_tarea.html', {'form': form, 'titulo_pagina': 'Crear nueva tarea'})

#Encargada de mostrar toda la lista de proyectos, ordenados por inicio
def pruebalistaproyecto(request):
    empleados =Proyecto.objects.order_by('id')
    context = {'lista_proyectos': empleados,
               'titulo_pagina':'Listado de proyectos'}
    return render(request, 'lista_proyectos.html', context)

#Encargada de mostrar un proyecto
class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto.html'

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del proyecto'
        return context
#Encargada de la creacion de tareas
class CrearProyecto(View):
    def get(self, request, *args, **kwargs):
        form = ProyectoForm()
        context = {
            'form' : form,
            'titulo_pagina' : 'Crear nuevo proyecto'
        }
        return render(request, 'crear_proyecto.html', context)

    def post(self, request, *args, **kwargs):
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
        return render(request, 'crear_proyecto.html', {'form': form, 'titulo_pagina': 'Crear nuevo proyecto'})
