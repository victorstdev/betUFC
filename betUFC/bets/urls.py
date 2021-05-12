from django.urls import path
from .views import EventoDetailView, EventoListView, EventoCreateView, EventoView

urlpatterns = [
    path('', EventoView.as_view(), name='index'),
    path('lista/', EventoListView.as_view(), name='lista_eventos'),
    path('visualizar/<int:pk>', EventoDetailView.as_view(), name='visualizar_evento'),
    path('criar/', EventoCreateView.as_view(), name='criar_evento'),
]
