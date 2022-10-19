from django.contrib import admin
from .models import Products
from django.contrib.auth.models import Group



admin.site.site_header = 'Autobots Control Dashboard'

# Register your models here.

admin.site.register(Products)
# admin.site.unregister(Group)
