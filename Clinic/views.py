from django.shortcuts import render, redirect

from .forms import userForm
from .models import Paciente


def index(request):
    return render(request, 'Clinic/index.html')


def registro_paciente(request):
    if request.method != 'POST':
        form = userForm()
    else:
        form = userForm(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.owner = request.user
            new_user.save()
            return redirect('Clinic/index.html')

    context = {'form': form}
    return render(request,'Clinic/registro_paciente.html', context)

# Create your views here.
