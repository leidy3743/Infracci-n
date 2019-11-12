# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from .forms import InfraccionCreateView, InfraccionUpdateView, InfraccionDeleteView, getSedes
from .views import InfraccionListView, InfraccionLista, InfraccionDetalle

urlpatterns = [

    url(r'^infraccion/crear$', InfraccionCreateView.as_view(), name='crear'),
    url(r'^infraccion/(?P<pk>\d+)/$', InfraccionUpdateView.as_view(), name='actualizar'), 
    url(r'^infraccion/listado$', InfraccionListView.as_view(), name='listar'),
    url(r'^infraccion/eliminar/(?P<pk>\d+)/$', InfraccionDeleteView.as_view(), name='eliminar'),
    url(r'^infraccion/crearInfraccion$', InfraccionLista.as_view(), name='crear'),
    url(r'^infraccion/detalleInfraccion/(?P<pk>[0-9]+)/$', InfraccionDetalle.as_view(), name='crear'),

]
