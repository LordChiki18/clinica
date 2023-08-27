from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import userForm
from .models import Paciente


def index(request):
    return render(request, 'Clinic/index.html')


@login_required
def getPacientes(request):
    users = Paciente.objects.filter(owner=request.user).order_by('fecha_nacimiento')
    context = {'users': users}
    return render(request, 'Clinic/users.html', context)


@login_required
def registro_paciente(request):
    if request.method != 'POST':
        form = userForm()
    else:
        form = userForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.owner = request.user
            new_user.save()
            return redirect('Clinic:getPacientes')

    context = {'form': form}
    return render(request, 'Clinic/registro_paciente.html', context)


def handler404(request, *args, **argv):
    """Método para manejar los errores 404"""
    response = render('learning_logs/404.html', {})
    response.status_code = 404
    return response
