# -*- encoding: utf-8 -*-

from django.views.generic import ListView
from .models import Infraccion
from inicio.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import InfraccionSerializer
from django.db.models.functions import Coalesce
from rest_framework.views import APIView
from rest_framework import generics

class InfraccionListView(LoginRequiredMixin, ListView):
	"""Lista todos las infracciones"""

	model = Infraccion
	context_object_name = 'infracciones'
	template_name = 'infraccion/infraccion_list.html'



class JSONResponse(HttpResponse):
	
    def __init__(self, data, **kwargs):
		contenido = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(contenido, **kwargs)


"""APIView: """
class InfraccionLista(APIView):

    def get(self, request, format=None):
        infraccion = Infraccion.objects.all()
        serializer = InfraccionSerializer(infraccion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InfraccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#APIView
class InfraccionDetalle(APIView):

    def get_object(self, pk):
        try:
            return Infraccion.objects.get(pk=pk)
        except Infraccion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        infraccion = self.get_object(pk)
        print(request)
        serializer = InfraccionSerializer(infraccion)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        infraccion = self.get_object(pk)
        serializer = InfraccionSerializer(infraccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        infraccion = self.get_object(pk)
        infraccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""class InfraccionLista(generics.ListCreateAPIView):
    queryset = Infraccion.objects.all()
    serializer_class = InfraccionSerializer


class InfraccionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Infraccion.objects.all()
    serializer_class = InfraccionSerializer"""


#APIView
"""class RegistroVehiculoUltimoSincronizado(APIView):
    def get(self, request, pk, format=None):
        consulta = RegistroVehiculo.objects.all().filter(peaje=pk).order_by(Coalesce('nombre_archivo', 'nombre_archivo').desc()).first()
        ultimo = str(consulta) + ".json"
        print(ultimo)
        context ={'ultimo': ultimo}
        return Response(context)"""