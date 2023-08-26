from django.urls import path
from . import views

app_name = 'Clinic'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    path('registro/', views.registro_paciente, name="registro_paciente"),
]