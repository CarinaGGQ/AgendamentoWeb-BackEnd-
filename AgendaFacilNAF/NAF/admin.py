from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'serviço', 'agendamento_disponivel', 'finalizado')
    list_filter = ('serviço', 'agendamento_disponivel__dia', 'finalizado')
    search_fields = ('cliente__nome', 'serviço__nome', 'agendamento_disponivel__dia')

@admin.register(AgendamentoDisponivel)
class AgendamentoDisponivelAdmin(admin.ModelAdmin):
    list_display = ('dia', 'hora')
    list_filter = ('dia',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')

@admin.register(Serviço)
class ServiçoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'serviço', 'feedback')
    search_fields = ('cliente__nome', 'serviço__nome', 'feedback')
