import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)
# app entrada
from applications.entrada.models import Entry
# models
from .models import Home
#forms
from .forms import SuscribersForm, ContacForm


class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Cargamos el home
        context['home']=Home.objects.latest('created')#es una funcion de django que trae el ultimo registro
        # contexto de portada
        context['portada'] = Entry.objects.entrada_en_portada()

        # contexto para los articulos en home
        context['entradas_home']=Entry.objects.entradas_en_home()

        # contexto para los articulos recientes
        context['entradas_recientes']=Entry.objects.entradas_recientes()
        # Enviamos formulario de suscripcion
        context['form']=SuscribersForm
        return context


class SuscriberCreateView(CreateView):
    form_class=SuscribersForm
    success_url='.'


class ContactCreateView(CreateView):
    form_class=ContacForm
    success_url='.'
    