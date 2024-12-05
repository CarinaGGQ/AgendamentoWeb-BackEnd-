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
    path('gerenciar_professor/', gerenciar_professor, name="gerenciar_professor"),
    path('gerenciar_aluno/', gerenciar_aluno, name="gerenciar_aluno"),
    path('gerenciar_administrador/', gerenciar_administrador, name="gerenciar_administrador"),
    path('confirmacao_sucesso/', confirmacao_sucesso, name="confirmacao_sucesso"),
    path('feedback_sucesso/', feedback_sucesso, name="feedback_sucesso"),
]
