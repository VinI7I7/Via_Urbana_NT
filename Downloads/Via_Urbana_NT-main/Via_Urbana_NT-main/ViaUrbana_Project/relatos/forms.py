from django import forms
from .models import Relato

class RelatoForm(forms.ModelForm):
    class Meta:
        model = Relato
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
        }   