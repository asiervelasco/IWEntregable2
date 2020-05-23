from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Empleado, Tarea, Proyecto, Cliente
from django.forms.models import model_to_dict
from django.views.generic import  DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


#Esta es nuestra API que vamos a utilizar para interactuar con la lista de clientes

@method_decorator(csrf_exempt, name='dispatch')
class ClientesCreación(View):
    def get(self, request):
        lista = Cliente.objects.all()
        return JsonResponse(list(lista.values()), safe=False)
    def post(self, request):
        nombre = request.POST["nombre"]
        cliente = Cliente()
        cliente.nombre = nombre
        cliente.save()
        return JsonResponse(model_to_dict(cliente))



def marcartareacomoFinalizada(req):
    tarea=Tarea.objects.get(pk=req.POST["id"])
    tarea.estado="Finalizada"
    tarea.save()
    return JsonResponse(model_to_dict(tarea))





#Funcion encargada de delvolver un email con los datos de los proyectos
def devolvermail(request):
    emailrec=request.POST['email']
    listaproyectos = Proyecto.objects.order_by('id')
    contenido=""
    tareas = Tarea.objects.all()
    for proyecto in listaproyectos:
        contenido=contenido+"Nombre del proyecto: "+proyecto.nombre + "\n"
        contenido = contenido + "Empleados del proyecto: "
        empleados=proyecto.empleados.all()
        for empleado in empleados :
            contenido=contenido+empleado.nombre+" "+empleado.apellido+","
        contenido=contenido + "\n"
        contenido = contenido + "Tareas asociadas a este proyecto: "
        for tarea in tareas:
            if tarea.proyecto==proyecto:
                contenido=contenido+tarea.nombre+","
        contenido = contenido + "\n"
        contenido = contenido +"Descripción del proyecto: "+proyecto.descripcion + "\n"
        contenido = contenido + "Nombre del cliente: " + proyecto.cliente.nombre + "\n"
        contenido = contenido + "Fecha de inicio: " + str(proyecto.inicio) + "\n"
        contenido = contenido + "Fecha de fin: " + str(proyecto.fin) + "\n"
        contenido = contenido + "Presupuesto: " + proyecto.presupuesto + "\n"+"\n"+"\n"

    send_mail('Hola desde el gestor de proyectos',
              contenido,
              'gestordeproyectosdeusto@gmail.com',
              [str(emailrec)],
              fail_silently=False)
    return  render(request, 'email.html')


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
        return context

#Las siguientes dos funciones se encargan de crear el formulario y de la creaciónd del empleado
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

#Encargado de la eliminación del empleado seleccionado
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



#Encargado de mostrar una única tarea
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea.html'
    def get_context_data(self, **kwargs):
        context = super(TareaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles de la tarea'
        context['titulo_pagina1'] = 'Detalles de la tarea'
        return context

#Encargada de mostrar toda la lista de tareas, ordenadas por id
def pruebalistatarea(request):
    tareas =Tarea.objects.order_by('proyecto')
    context = {'lista_tareas': tareas,
               'titulo_pagina':'Listado de tareas',
                'titulo_pagina1': 'Listado de tareas'}
    return render(request, 'lista_tareas.html', context)

#Encargada de la creacion de el formulario de creación de tareas
def showform_proy1(request):
    listaempleados = Empleado.objects.order_by('id')
    listaproyectos = Proyecto.objects.order_by('id')
    context = {'listaempleados': listaempleados,
               'listaproyectos': listaproyectos}
    
    context['titulo_pagina'] = 'Crear tarea'
    context['titulo_pagina1'] = 'Crear tarea'
    return render(request, 'crear_tarea.html', context)

#Encargada de la creacion de las tareas
def creartarea(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    inicio = request.POST["inicio"]
    fin = request.POST["fin"]
    prioridad = request.POST["prioridad"]
    estado = request.POST["estado"]
    notas = request.POST["notas"]
    tarea = Tarea()
    tarea.nombre = nombre
    tarea.descripcion = descripcion
    tarea.inicio = inicio
    tarea.fin = fin
    tarea.prioridad = prioridad
    tarea.estado = estado
    tarea.notas = notas
    listaempleados = request.POST["responsable"]
    for id in listaempleados:
        empleado = Empleado.objects.get(pk=id)
        tarea.responsable=empleado
    listaproyectos = request.POST["proyecto"]
    for id in listaproyectos:
        proyecto = Proyecto.objects.get(pk=id)
        tarea.proyecto=proyecto
    tarea.save()
    return redirect('listatareas')

#Encargada de la eliminación de tareas
class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'eliminar_Tarea.html'
    success_url = reverse_lazy('listatareas')

#Encargada de la modificación de tareas
class TareaUpdateView(UpdateView):
    model = Tarea
    fields = '__all__'
    listaempleados = Empleado.objects.order_by('id')
    context = {'listaempleados': listaempleados}
    template_name = 'modificar_tarea.html'
    success_url = reverse_lazy('listatareas')



#Encargada de mostrar toda la lista de proyectos, ordenados por inicio
def pruebalistaproyecto(request):
    proyectos = Proyecto.objects.order_by('id')
    context = {'lista_proyectos': proyectos,
               'titulo_pagina':'Gestor de proyectos',
               'titulo_pagina1':'Gestion de proyectos'}
    return render(request, 'lista_proyectos.html', context)

#Encargada de mostrar un proyecto en detalle
def proyectodetalles (request,id):
    proyecto=get_object_or_404(Proyecto, pk=id)
    empleados = proyecto.empleados.all()
    tareas =Tarea.objects.all()
    textempl=""
    for empleado in empleados:
        textempl=textempl+empleado.nombre+" "+empleado.apellido+", "
    context={'proyecto':proyecto, 'empleados':textempl,'titulo_pagina':'Detalles de proyecto',
               'titulo_pagina1':'Detalles de proyecto',
               'tareas':tareas}
    return render(request,'proyecto.html', context)

#Encargada de la creacion del formulario de proyectos
def showform_proy(request):
    listaempleados = Empleado.objects.order_by('id')
    listaclientes = Cliente.objects.order_by('id')
    context = {'listaempleados': listaempleados,
               'listaclientes': listaclientes}

    context['titulo_pagina'] = 'Crear proyecto'
    context['titulo_pagina1'] = 'Crear proyecto'
    return render(request, 'crear_proyecto.html', context)

#Encargada de la creación de proyectos
def crearproyecto(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    inicio = request.POST["inicio"]
    fin = request.POST["fin"]
    presupuesto = request.POST['presupuesto']
    proyecto = Proyecto()
    proyecto.nombre = nombre
    proyecto.descripcion = descripcion
    proyecto.inicio = inicio
    proyecto.fin = fin
    proyecto.presupuesto = presupuesto
    Listaempleados = request.POST.getlist("empleados")
    clienteid = request.POST["cliente"]
    cliente = Cliente.objects.get(pk=int(clienteid))
    proyecto.cliente = cliente
    proyecto.save()
    for cosa in Listaempleados:
        empleado = Empleado.objects.get(pk=cosa)
        proyecto.empleados.add(empleado)
    proyecto.save()
    return redirect('listaproyectos')

#Encargada de la eliminación de proyectos
class ProyectosDeleteView(DeleteView):
    model = Proyecto
    template_name = 'eliminar_proyecto.html'
    success_url = reverse_lazy('listaproyectos')

#Encargada de la modificación de proyectos
class ProyectosUpdateView(UpdateView):
    model = Proyecto
    fields = '__all__'
    listaempleados = Empleado.objects.order_by('id')
    context = {'listaempleados': listaempleados}
    template_name = 'modificar_proyecto.html'
    success_url = reverse_lazy('listaproyectos')



#Encargada de mostrar toda la lista de clientes, ordenados por id
def pruebalistaclientes(request):
    cliente = Cliente.objects.order_by('id')
    context = {'lista_clientes': cliente,
               'titulo_pagina':'Listado de clientes',
               'titulo_pagina1':'Listado de clientes'}
    return render(request, 'lista_clientes.html', context)

#Encargado de mostrar un único cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente.html'
    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles del cliente'
        context['titulo_pagina1'] = 'Detalles del cliente'
        return context

#Las siguientes dos funciones se encargan de crear el formulario y de la creación del cliente
def show_formC(request):
    return render(request, 'crear_cliente.html')

def crearCliente(request):
    nombre = request.POST["nombre"]
    cliente = Cliente()
    cliente.nombre = nombre
    cliente.save()
    return redirect('listaclientes')

#Encargado de la eliminación del cliente seleccionado
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'eliminar_cliente.html'
    success_url = reverse_lazy('listaclientes')

#Encargada de actualizar el cliente seleccionado
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'modificar_cliente.html'
    success_url = reverse_lazy('listaclientes')