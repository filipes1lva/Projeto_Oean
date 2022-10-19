from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

CATEGORIA = (
    ('Estacionário', 'Estacionário'),
    ('Eletrônicos', 'Eletrônicos'),
    ('Alimentos', 'Alimentos'),
)


class Products(models.Model):
    nome = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    quantidade = models.PositiveBigIntegerField(null=True)

    def __str__(self) -> str:
        return f'{self.nome}-{self.quantidade}'
