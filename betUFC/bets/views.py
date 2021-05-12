from django.shortcuts import render, Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Evento
from .forms import InserirEventoForm
# Create your views here.

class EventoView(TemplateView):
    template_name = "index.html"


class EventoListView(ListView):
    model = Evento
    template_name = "lista_eventos.html"
    context_object_name = 'eventos'

class EventoDetailView(DetailView):
    model = Evento
    template_name = "detalhes_evento.html"
    context_object_name = 'evento'

class EventoCreateView(CreateView):
    model = Evento
    template_name = "criar_evento.html"
    form_class = InserirEventoForm
    success_url = reverse_lazy("lista_eventos")
