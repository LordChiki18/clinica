from django.db import models

# Create your models here.


class Paciente(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


class Rac(models.Model):
    Frecuencia = models.CharField(max_length=200)
    Presion = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Frecuencia, self.Presion
