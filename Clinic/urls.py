from django.urls import path
from . import views

app_name = 'Cinic'
urlpatterns = [
    #Home Page
    path('', views.index, name='index')
]