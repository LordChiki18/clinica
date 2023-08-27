from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import userForm, racForm
from .models import Paciente, Rac


def index(request):
    return render(request, 'Clinic/index.html')


@login_required
def getPacientes(request):
    pacientes = Paciente.objects.filter(owner=request.user).order_by('date_added')
    context = {'pacientes': pacientes}
    return render(request, 'Clinic/pacientes.html', context)


@login_required
def getPaciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)

    if paciente.owner != request.user:
        raise Http404
    datos = Rac.objects.filter(paciente=paciente).order_by('-date_added')
    context = {
        'paciente': paciente,
        'datos': datos
    }
    return render(request, 'Clinic/paciente.html', context)


@login_required
def newPaciente(request):
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
    return render(request, 'Clinic/newPaciente.html', context)


@login_required
def newRac(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if paciente.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = racForm()
    else:
        form = racForm(data=request.POST)
        if form.is_valid():
            new_rac = form.save(commit=False)
            new_rac.paciente = paciente
            new_rac.save()
            return redirect('Clinic:getPaciente', paciente_id=paciente_id)

    context = {'paciente': paciente, 'form': form}
    return render(request, 'Clinic/newRac.html', context)


@login_required
def editRac(request, rac_id):
    rac = Rac.objects.get(id=rac_id)
    paciente = rac.paciente
    if paciente.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = racForm(instance=rac)
    else:
        form = racForm(instance=rac, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clinic:getPaciente', paciente_id=paciente.id)

    context = {'rac': rac, 'paciente': paciente, 'form': form}
    return render(request, 'Clinic/editRac.html', context)


@login_required
def removeRac(request, rac_id):
    rac = Rac.objects.get(id=rac_id)
    paciente = rac.paciente
    if paciente.owner != request.user:
        raise Http404
    rac.delete()
    return redirect('Clinic:getPaciente', paciente_id=paciente.id)


@login_required
def editPaciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if paciente.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = userForm(instance=paciente)
    else:
        form = userForm(instance=paciente, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clinic:getPaciente')

    context = {'paciente': paciente, 'form': form}
    return render(request, 'Clinic/editPaciente.html', context)


@login_required
def removePaciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    if paciente.owner != request.user:
        raise Http404
    paciente.delete()
    return redirect('Clinic:getPacientes')


def handler404(request, *args, **argv):
    """Método para manejar los errores 404"""
    response = render('learning_logs/404.html', {})
    response.status_code = 404
    return response
