# -*- encoding: utf-8 -*-
from django.shortcuts import render
import requests
import json
from django.core.serializers.json import DjangoJSONEncoder

def getSedes():
	url='http://fredyball.pythonanywhere.com/api/sedes/?format=json'
	respuesta=requests.get('http://fredyball.pythonanywhere.com/api/sedes/?format=json')
	sedes=respuesta.json()
	sedes2 = json.dumps(list(sedes), cls=DjangoJSONEncoder)
	print(sedes2)
	sedes_list={'sedes2':sedes2}
