from django.contrib import admin
from .models import Contato, Pessoa


@admin.action(description='Ativar todas as pessoas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.action(description='Desativar todas as pessoas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo', 'data_nasc', 'ativo',
    ]

    list_editable = [
        'data_nasc', 'ativo',
    ]

    actions = [
        ativar_todos, desativar_todos
    ]


@admin.register(Contato)
class ConntatoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'email', 'telefone', 'pessoa',
    ]

    list_editable = [
        'email', 'telefone', 'pessoa',
    ]
