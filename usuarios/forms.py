from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioCustomizado

class CadastroUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioCustomizado
        fields = UserCreationForm.Meta.fields + ('email',) 
                                                          