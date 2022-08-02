from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.ListaPessoaView.as_view()), name='pessoa.index'),  # noqa
    path('novo/', login_required(views.PessoaCreateView.as_view()), name='pessoa.novo'),  # noqa
    path('editar/<int:pk>', login_required(views.PessoaUpdateView.as_view()), name='pessoa.editar'),  # noqa
    path('deletar/<int:pk>', login_required(views.PessoaDeleteView.as_view()), name='pessoa.deletar'),  # noqa
    path('contatos/<int:pk_pessoa>', login_required(views.contatos), name='pessoa.contatos'),  # noqa
    path('contato/novo/<int:pk_pessoa>', login_required(views.contato_novo), name='contato.novo'),  # noqa
    path('contato/<int:pk_pessoa>/editar/<int:pk>', login_required(views.contato_editar), name='contato.editar'),  # noqa
    path('contato/<int:pk_pessoa>/remover/<int:pk>', login_required(views.contato_remover), name='contato.remover'),  # noqa
]
