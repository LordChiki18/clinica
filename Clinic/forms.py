from django import forms
from .models import Paciente, Rac


class userForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido']
        labels = {
            'nombre': 'Nombre',  # Puedes establecer la etiqueta que desees aquí
            'apellido': 'Apellido',  # Puedes establecer la etiqueta que desees aquí
        }


class racForm(forms.ModelForm):

    class Meta:
        model = Rac
        fields = ['Frecuencia', 'Presion', 'edad', 'fecha_nacimiento']
        labels = {
            'Frecuencia': 'Frecuencia',
            'Presion': 'Presion',
            'edad': 'Edad',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'placeholder': 'AAAAMMDD'}),
        }
