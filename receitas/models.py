from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_da_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=True)

