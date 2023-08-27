

from django.urls import path
from . import views

app_name = 'Clinic'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Pagina para mostrar todos los pacientes
    path('usuario/', views.getPacientes, name="getPacientes"),
    # Pagina para mostrar detalles de un paciente
    path('usuario/<int:paciente_id>/', views.getPaciente, name="getPaciente"),
    # Pagina para crear un nuevo paciente
    path('registro/', views.newPaciente, name="newPaciente"),
    # Pagina para crear un nuevo Rac
    path('new_rac/<int:paciente_id>/', views.newRac, name="newRac"),
    # Pagina para editar un nuevo Rac
    path('edit_rac/<int:rac_id>/', views.editRac, name='editRac'),
    # Pagina para eliminar un nuevo Rac
    path('remove_rac/<int:rac_id>', views.removeRac, name='removeRac'),
    # Pagina para editar un usuario
    path('edit_usuario/<int:paciente_id>', views.editPaciente, name='editPaciente'),
    # Pagina para eliminar un usuario
    path('remove_paciente/<int:paciente_id>', views.removePaciente, name='removePaciente'),
]
