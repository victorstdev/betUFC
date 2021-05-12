from django import forms
from .models import Evento

class InserirEventoForm(forms.ModelForm):
    
    class Meta:
        model = Evento
        fields = '__all__'
