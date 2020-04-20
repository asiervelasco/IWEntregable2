from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Empleado, Tarea, Proyecto
from .forms import EmpleadoForm, TareaForm, ProyectoForm
from django.views.generic import ListView, DetailView

def index(request):
    return HttpResponse("Listado de departamentos")

class EmpleadoListView(ListView):
    model = Empleado
    queryset = Empleado.objects.order_by('dni')
    template_name = "lista_empleados.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Listado de empleados'
        return context

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del empleado'
        return context

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

