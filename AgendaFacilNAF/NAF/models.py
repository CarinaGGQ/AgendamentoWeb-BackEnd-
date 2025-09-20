from django.db import models
from django.contrib.auth.models import User

# ---------------- CLIENTE ----------------
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.nome)


# ---------------- SERVIÇO ----------------
class Serviço(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.nome)


# ---------------- LISTA DE HORÁRIOS ----------------
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


# ---------------- AGENDAMENTO DISPONÍVEL ----------------
class AgendamentoDisponivel(models.Model):
    dia = models.DateField(null=False, blank=False)
    hora = models.CharField(max_length=5, choices=LISTA_HORARIOS)

    def __str__(self):
        return f"{self.dia}, {self.hora}"


# ---------------- FEEDBACK ----------------
class Feedback(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    serviço = models.ForeignKey(Serviço, null=False, blank=False, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=2000, null=False, blank=False, default='DEFAULT VALUE')

    def __str__(self):
        return f"Cliente: {self.cliente.nome}, Serviço: {self.serviço.nome}, Feedback: {self.feedback}"


# ---------------- AGENDAMENTO ----------------
class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    serviço = models.ForeignKey(Serviço, null=False, blank=False, on_delete=models.CASCADE)
    agendamento_disponivel = models.ForeignKey(AgendamentoDisponivel, null=False, blank=False, on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        # Corrigir para usar o nome correto do campo: agendamento_disponivel
        return f"Cliente: {self.cliente.nome}, Serviço: {self.serviço.nome}, Agendamento: {self.agendamento_disponivel.dia} - {self.agendamento_disponivel.hora}"