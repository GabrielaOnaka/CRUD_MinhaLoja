from django.db import models


class Pessoa(models.Model):
    objects = None
    nome = models.CharField(max_length=60, null=True)
    cpf = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=60, null=True)
    endereco = models.CharField(max_length=80, null=True)
    cidade = models.CharField(max_length=60,null=True)
    uf = models.CharField(max_length=2,null=True)

    def __str__(self) -> str:
        return self.nome
