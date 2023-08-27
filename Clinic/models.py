from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Rac(models.Model):
    Frecuencia = models.CharField(max_length=200)
    Presion = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Frecuencia, self.Presion
