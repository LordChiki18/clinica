from django.contrib import admin

# Register your models here.
from .models import Rac, Paciente

admin.site.register(Rac)
admin.site.register(Paciente)