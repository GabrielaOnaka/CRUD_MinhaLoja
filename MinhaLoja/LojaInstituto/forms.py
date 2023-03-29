from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ('nome', 'cpf', 'email', 'endereco', 'cidade')