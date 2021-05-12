from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

METODOS = [
    ('UD','Decisão Unânime'),
    ('SD','Decisão Dividida'),
    ('MD','Decisão Majoritária'),
    ('TKO','Nocaute Técnico'),
    ('KO','Nocaute'),
    ('SUB','Finalização'),
]

class Evento(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Lutador(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Luta(models.Model):  
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    vencedor = models.ForeignKey(Lutador, on_delete=models.CASCADE, related_name='vencedor')
    perdedor = models.ForeignKey(Lutador, on_delete=models.CASCADE, related_name='perdedor')
    metodo = models.CharField(choices=METODOS, max_length=50)
    assalto = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    def __str__(self):
        return self.vencedor + " VS " + self.perdedor