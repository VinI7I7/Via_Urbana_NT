from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RelatoForm
from .models import Relato

@login_required(login_url='/usuarios/login/')
def fazer_relato(request):
    if request.method == 'POST':
        form = RelatoForm(request.POST)
        if form.is_valid():
            relato = form.save(commit=False)
            relato.usuario = request.user
            relato.save()
            return redirect('meus_relatos')
    else:
        form = RelatoForm()

    return render(request, 'relatos/fazer_relato.html', {'form': form})


@login_required(login_url='/usuarios/login/')
def meus_relatos(request):
    relatos = Relato.objects.filter(usuario=request.user)
    return render(request, 'relatos/meus_relatos.html', {'relatos': relatos})
