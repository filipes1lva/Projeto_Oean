# Generated by Django 4.1.2 on 2022-10-20 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Produtos'},
        ),
    ]