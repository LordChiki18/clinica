from django import forms
from .models import Paciente


class userForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento']
        labels = {
            'nombre': 'Nombre',  # Puedes establecer la etiqueta que desees aquí
            'apellido': 'Apellido',  # Puedes establecer la etiqueta que desees aquí
            'edad': 'Edad',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }