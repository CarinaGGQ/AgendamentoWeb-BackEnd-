from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.nome)
    
class Serviço(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nome)

LISTA_HORARIOS = (
    ("9h", "9h às 10h"),
    ("10h", "10h às 11h"),
    ("11h", "11h às 12h"),
    ("12h", "12h às 13h"),
    ("13h", "13h às 14h"),
    ("14h", "14h às 15h"),
    ("15h", "15h às 16h"),
    ("16h", "16h às 17h"),
    ("17h", "17h às 18h"),
)



class AgendamentoDisponivel(models.Model):
    dia = models.DateField(null=False, blank=False)
    hora = models.CharField(max_length=5, choices=LISTA_HORARIOS)

    def __str__(self):
        return f"{self.dia}, {self.hora}"

class Feedback(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    serviço = models.ForeignKey(Serviço, null=False, blank=False, on_delete=models.CASCADE)


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    serviço = models.ForeignKey(Serviço, null=False, blank=False, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    AgendamentoDisponivel = models.ForeignKey(AgendamentoDisponivel, null=False, blank=False, on_delete=models.CASCADE)

