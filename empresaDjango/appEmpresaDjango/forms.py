from django import forms
from .models import Empleado, Tarea, Proyecto, Cliente

#Lista de forms que vamos a utilizar

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'