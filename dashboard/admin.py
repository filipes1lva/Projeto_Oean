from django.contrib import admin
from .models import Products, Order
from django.contrib.auth.models import Group


admin.site.site_header = 'Autobots Control Dashboard'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'categoria')
    list_filter = ['categoria']


# Register your models here.

admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)

