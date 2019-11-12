# -*- encoding: utf-8 -*-

from django.contrib import admin
from .models import Infraccion

class InfraccionAdmin(admin.ModelAdmin):

	list_display = ('numero', 'sede', 'descripcion', 'placa', 'fecha')

	search_fields = ('numero', 'sede')

admin.site.register(Infraccion, InfraccionAdmin)