from django import forms
from .models import Paciente

class userForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['usuario', 'password', 'nombre', 'apellido']
        labels = {
            'usuario': 'Usuario',  # Puedes establecer la etiqueta que desees aquí
            'password': 'Password',  # Puedes establecer la etiqueta que desees aquí
            'nombre': 'Nombre',  # Puedes establecer la etiqueta que desees aquí
            'apellido': 'Apellido',  # Puedes establecer la etiqueta que desees aquí
        }
        widgets = {
            'password': forms.PasswordInput(),  # Por ejemplo, para ocultar el campo de contraseña
        }
