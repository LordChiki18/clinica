from django.urls import path
from . import views

app_name = 'Clinic'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Pagina para ver usuarios
    path('usuario/', views.getPacientes, name="getPacientes"),
    # Pagina para registro de usuarios
    path('registro/', views.registro_paciente, name="registro_paciente"),
]
