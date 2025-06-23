from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RelatoForm
from .models import Relato
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required(login_url='/usuarios/login/')
def fazer_relato(request):
    if request.method == 'POST':
        form = RelatoForm(request.POST, request.FILES)  
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
    relatos = Relato.objects.filter(usuario=request.user).order_by('-data_criacao')
    return render(request, 'relatos/meus_relatos.html', {'relatos': relatos})


@login_required(login_url='/usuarios/login/')
def resumo_relatos(request):
    if request.user.username != 'admin':
        return HttpResponseForbidden("Acesso negado.")
    relatos = Relato.objects.all().order_by('-data_criacao')
    return render(request, 'relatos/resumo_relatos.html', {'relatos': relatos})


@require_POST
def alterar_status(request, relato_id):
    relato = get_object_or_404(Relato, id=relato_id)
    status_atualizado = request.POST.get('status')
    status_validos = [choice[0] for choice in Relato.STATUS_RELATOS]

    if status_atualizado not in status_validos:
        messages.error(request, "Status inválido.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    relato.status = status_atualizado
    relato.save()
    messages.success(request, f"Status do relato '{relato.titulo}' atualizado para {status_atualizado}.")
    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_POST
def excluir_relato(request, id):
    relato = get_object_or_404(Relato, id=id)
    relato.delete()
    messages.success(request, "Relato excluído com sucesso!")
    return redirect(request.META.get('HTTP_REFERER', '/'))
