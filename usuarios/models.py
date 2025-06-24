from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioCustomizado(AbstractUser):
    #aqui pode adicionar campos adicionais se necessário
    pass

    def __str__(self):
        return self.username

