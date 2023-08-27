from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Rac(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Frecuencia = models.CharField(max_length=200)
    Presion = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name_plural = 'datos'

    def __str__(self):
        return f"{self.Frecuencia} {self.Presion}"
