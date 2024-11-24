from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Serviço)
admin.site.register(AgendamentoDisponivel)
admin.site.register(Feedback)
admin.site.register(Agendamento)
