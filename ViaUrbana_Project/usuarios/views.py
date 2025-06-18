from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CadastroUsuarioForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CadastroUsuarioForm()
    # Mude esta linha:
    return render(request, 'registro.html', {'form': form}) 
