from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('aluno/', aluno, name="aluno"),
    path('professor/', professor, name="professor"),
    path('administrador/', administrador, name="administrador"),
    path('feedback/', feedback, name="feedback"),
    path('agendamento/', agendamento, name="agendamento"),
    path('confirmacao/', confirmacao, name="confirmacao"),
    path('fazer_login/', fazer_login, name="fazer_login"),
    path('gerenciar/', gerenciar, name="gerenciar"),
]
