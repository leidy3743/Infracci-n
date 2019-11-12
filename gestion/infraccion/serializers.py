# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import serializers
from .models import Infraccion

"""Django Rest Framework: Es un conjunto de herramientas de gran alcance y flexible que 
hace que sea fácil la construcción de  APIs Web. Este framework adicionalmente cuenta 
con la capacidad de poder liberar el API de manera que pueda ser navegado y utilizado 
para ejecutar ejemplos directamente desde nuestro navegador web y probar la funcionalidad
de los servicios que vayamos necesitando. 

Serializadores: Los serializadores permiten convertir datos complejos como conjuntos de
consultas e instancias de modelos a tipos de datos nativos de Python que luego se pueden
representar fácilmente en JSON, XML u otros tipos de contenido"""
class InfraccionSerializer(serializers.ModelSerializer):
	"""Define la organización de los datos del registro de un vehiculo que se mostrarán 
	en el modelo del serializador"""

	"""Permite mostrar los campos que se obtendran o enviaran por medio del serializador
	al servidor"""	
	class Meta:
		model = Infraccion
		fields = ('numero', 'sede', 'descripcion', 'placa', 'fecha')
