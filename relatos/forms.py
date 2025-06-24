from django import forms
from .models import Relato

class RelatoForm(forms.ModelForm):
    class Meta:
        model = Relato
        fields = ['titulo', 'tipo', 'categoria', 'descricao', 'localizacao', 'foto']
