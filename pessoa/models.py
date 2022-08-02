from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nasc = models.DateField(null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_completo


class Contato(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome