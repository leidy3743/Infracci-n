# -*- encoding: utf-8 -*-

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.template import loader
from django.template import Context
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from django.views import generic
from inicio.mixins import LoginRequiredMixin
from .models import Infraccion
from django.shortcuts import render
import json
import services
from django.shortcuts import render
import requests
from django.core.serializers.json import DjangoJSONEncoder


def getSedes():
	url='http://fredyball.pythonanywhere.com/api/sedes/?format=json'
	respuesta=requests.get(url)
	sedes=respuesta.json()
	sedes2 = json.dumps(list(sedes), cls=DjangoJSONEncoder)
	print(sedes2)
	sedes_list={'sedes2':sedes2}
	
"""class getSedes(generic.TemplateView):
	def get(self, request):
		sedes_list=services.getSedes()
		print("AQUI"+str(sedes_list))
		#return Response(sedes_list)
		return render(request, 'infraccion/infraccion_list.html', sedes_list)"""

class InfraccionCreateView(LoginRequiredMixin, CreateView):
	getSedes()
	model = Infraccion
	fields = ['numero', 'sede', 'descripcion', 'placa', 'fecha']

	def get_context_data(self,**kwargs):
		context = super(InfraccionCreateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Crear Infracción'
		context['button_text'] = 'Crear'
		return context

	def get_success_url(self):
		messages.info(self.request,"La infracción ha sido creada con exito")
		return reverse_lazy('infraccion:listar')


class InfraccionUpdateView(LoginRequiredMixin, UpdateView):
	model = Infraccion
	fields = ['numero', 'sede', 'descripcion', 'placa', 'fecha']
	success_url = reverse_lazy('infraccion:listar')

	def get_context_data(self,**kwargs):
		context = super(InfraccionUpdateView,self).get_context_data(**kwargs)
		context['section_title'] = 'Actualizar Infraccion'
		context['button_text'] = 'Actualizar'
		return context

	def get_success_url(self):
		messages.info(self.request,"La infracción ha sido actualizada con exito")
		return reverse_lazy('infraccion:listar')


class InfraccionDeleteView(LoginRequiredMixin, DeleteView):
	
	model = Infraccion
	template_name = 'infraccion/infraccion_confirm_delete.html'
	success_url = reverse_lazy('infraccion:listar')