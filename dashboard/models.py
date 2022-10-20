from pickle import TRUE
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


from dashboard.views import staff

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

    
    class Meta:
        verbose_name_plural = 'Produtos'



    def __str__(self) -> str:
        return f'{self.nome}-{self.quantidade}'


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Pedidos'



    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
