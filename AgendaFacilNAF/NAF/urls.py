from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('aluno/', fazer_login, name="aluno"),
    path('professor/', fazer_login, name="professor"),
    path('administrador/', fazer_login, name="administrador"),
    path('feedback/', feedback, name="feedback"),
    path('agendamento/', agendamento, name="agendamento"),
    path('confirmacao/', confirmacao, name="confirmacao"),
    path('fazer_login/', fazer_login, name="fazer_login"),
    path('gerenciar/', gerenciar, name="gerenciar"),
    path('gerenciar/', gerenciar_professor, name="gerenciar_professor"),
    path('gerenciar/', gerenciar_aluno, name="gerenciar_aluno"),
    path('gerenciar/', gerenciar_administrador, name="gerenciar_administrador"),
]
