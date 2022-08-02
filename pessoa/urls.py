from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListaPessoaView.as_view(), name='pessoa.index'),
    path('novo/', views.PessoaCreateView.as_view(), name='pessoa.novo'),
    path('editar/<int:pk>', views.PessoaUpdateView.as_view(), name='pessoa.editar'),  # noqa
    path('deletar/<int:pk>', views.PessoaDeleteView.as_view(), name='pessoa.deletar'),  # noqa
    path('contatos/<int:pk_pessoa>', views.contatos, name='pessoa.contatos'),
    path('contato/novo/<int:pk_pessoa>', views.contato_novo, name='contato.novo'),  # noqa
    path('contato/<int:pk_pessoa>/editar/<int:pk>', views.contato_editar, name='contato.editar'),  # noqa
    path('contato/<int:pk_pessoa>/remover/<int:pk>', views.contato_remover, name='contato.remover'),  # noqa
]
