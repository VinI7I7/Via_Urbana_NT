from django.db import models
from django.conf import settings

class Relato(models.Model):
    TIPOS_RELATOS = [
        ('Reclamação', 'Reclamação'),
        ('Elogio', 'Elogio'),
        ('Sugestão', 'Sugestão'),
    ]

    CATEGORIAS = [
        ('Transporte Público', 'Transporte Público'),
        ('Vias urbanas', 'Vias Urbanas'),
        ('Outros', 'Outros'),
    ]

    STATUS_RELATOS= [
        ('Pendente', 'Pendente'), 
        ('Em análise', 'Em análise'),
        ('Em execução', 'Em execução'),
        ('Concluído', 'Concluído')
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS_RELATOS)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_RELATOS, default='Pendente')

    def __str__(self):
        return self.titulo
