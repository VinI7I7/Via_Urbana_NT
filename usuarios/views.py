from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CadastroUsuarioForm
from django.http import HttpResponseForbidden


def registrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'registro.html', {'form': form}) 

@login_required (login_url='/usuarios/login/')
def redirecionar_usuario(request):
    if request.user.username == 'admin' or request.user.email =='admin@email.com.br':
        return redirect('home_admin')
    else :
        return redirect('home')
    
@login_required (login_url='/usuarios/login/')
def home_admin(request):
    if request.user.username != 'admin' :
        return HttpResponseForbidden("Acesso negado.")
    return render(request, 'home_admin.html')