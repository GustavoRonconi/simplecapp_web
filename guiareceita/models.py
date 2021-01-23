from django.db import models


class ClassificacaoViagem(models.Model):
    id = models.AutoField(primary_key=True)
    classificacao = models.CharField(max_length=100, null=True)


class Viagem(models.Model):
    id = models.AutoField(primary_key=True)
    data_inicio = models.DateTimeField(null=False)
    data_fim = models.DateTimeField(null=False)
    classificacao = models.OneToOneField(
        ClassificacaoViagem, blank=True, null=True, on_delete=models.CASCADE
    )
    nota = models.IntegerField(null=True)
