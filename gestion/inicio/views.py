# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordResetForm
from django.db.models import Count, Sum
from django.contrib.auth.views import password_reset, password_reset_confirm
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db.models.functions import Coalesce
from persona.models import Persona, USUARIO, ADMINISTRADOR
import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from datetime import date

# Create your views here.

class Login(TemplateView):

	#Cuando la peticion es tipo GET, se muestra el template de login
	def get(self,request,*args,**kwargs):
		#Si el usuario esta autenticado, se le muestra su perfil
		if request.user.is_authenticated() and not request.user.is_staff:
			return self.get_user_template(request)
		#En caso de que no este autenticado, se le muestra el formulario de login
		else:
			return render(request, 'inicio/contenido_login.html')

	#Cunado la peticion es tipo POST se hace el proceso de login con la informacion del formulario de login
	def post(self,request,*args,**kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')

		#Usando el la funcion authenticate, obtenemos el usuario que corresponde con los datos
		#pasados como argumentos
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)

				#Retornamos una respuesta con el perfil del usuario
				return self.get_user_template(request)
			else:
				context = {'message':'Su usuario no esta activo'}
				return render(request, 'inicio/contenido_login.html', context)
		else:
			context = {'message':'Usuario o contraseña invalido'}
			return render(request, 'inicio/contenido_login.html', context)

	def get_user_template(self,request):
		if request.user.persona.tipo == ADMINISTRADOR:

			context = {
				}
			return render(request, 'cuenta/perfil_administrador.html', context)

		elif request.user.persona.tipo == USUARIO:
			#MENU USUARIO
			num_empleados = Persona.objects.all().count()
			num_productos = Producto.objects.all().count()

			context = {
				'num_empleados':num_empleados,
				'num_productos':num_productos,
				}
			return render(request, 'cuenta/perfil_usuario.html', context)


class Logout(TemplateView):

	def dispatch(self,request,*args,**kwargs):
		logout(request)
		context = {}
		return render(request, 'inicio/contenido_login.html', context)


class RecuperarLogin(TemplateView):

	def dispatch(self,request,*args,**kwargs):
		return password_reset(
			request, 
			template_name = 'inicio/recuperar_login_form.html',
			email_template_name = 'inicio/recuperar_login_email.html',
			subject_template_name = 'inicio/recuperar_login_email_asunto.txt',
			post_reset_redirect = reverse('inicio:recuperar_login_email_enviado'))


class RecuperarLoginEmailEnviado(TemplateView):

	def dispatch(self,request,*args,**kwargs):
		return render(request,'inicio/recuperar_login_email_enviado.html')


class RecuperarLoginConfirmacion(TemplateView):

	def dispatch(self,request,*args,**kwargs):

		return password_reset_confirm(
			request,
			template_name = 'inicio/recuperar_login_confirmacion.html',
			uidb64=kwargs['uidb64'], token=kwargs['token'],
			post_reset_redirect=reverse('inicio:recuperar_login_terminado'))


class RecuperarLoginTerminado(TemplateView):

	def dispatch(self,request,*args,**kwargs):
		return render(request, 'inicio/recuperar_login_terminado.html')