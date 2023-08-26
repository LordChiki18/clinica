from django import forms
from .models import Paciente, Rac

class user_form(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['']