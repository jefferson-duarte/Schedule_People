from django import forms
from .models import Contato, Pessoa


class PessoaForm(forms.ModelForm):
    data_nasc = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )

    class Meta:
        model = Pessoa
        fields = [
            'nome_completo', 'data_nasc', 'ativo',
        ]


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome', 'email', 'telefone'
        ]
