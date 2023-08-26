from django import forms
from .models import Paciente

class userForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['usuario', 'password', 'nombre', 'apellido']
        labels = {
            'usuario': '',  # Puedes establecer la etiqueta que desees aquí
            'password': '',  # Puedes establecer la etiqueta que desees aquí
            'nombre': '',  # Puedes establecer la etiqueta que desees aquí
            'apellido': '',  # Puedes establecer la etiqueta que desees aquí
        }
        widgets = {
            'password': forms.PasswordInput(),  # Por ejemplo, para ocultar el campo de contraseña
        }
