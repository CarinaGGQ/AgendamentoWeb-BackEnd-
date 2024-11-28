from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email

# Create your views here.
def homepage(request):
  return render(request, 'homepage.html')

def aluno(request):
  return render(request, 'colaborador/aluno.html')

def professor(request):
  return render(request, 'colaborador/professor.html')

def administrador(request):
  return render(request, 'colaborador/administrador.html')

def feedback(request):
  return render(request, 'feedback.html')

def agendamento(request):
  return render(request, 'agendamento.html')

def confirmacao(request):
  return render(request, 'confirmacao.html')


def fazer_login(request):
  erro = False
  
  if request.method == "POST":
    dados = request.POST.dict()
    if "username" in dados and "password" in dados:
      username = dados.get("username")
      password = dados.get("password")
      usuario = authenticate(request, username=username, password=password)
      if usuario:
        login(request, usuario)
        return render(request, 'colaborador/gerenciar.html')
      else:
        erro = True
    else:
      erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/fazer_login.html', context)

def gerenciar(request):
  return render(request, 'gerenciar.html')

@login_required
def gerenciar_professor(request):
  erro = False
  if request.user.groups.filter(name="professores").exists():
    return render(request, 'colaborador/gerenciar.html')
  erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/professor.html', context)

@login_required
def gerenciar_aluno(request):
  erro = False
  if request.user.groups.filter(name="alunos").exists():
    return render(request, 'colaborador/gerenciar.html')
  erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/aluno.html', context)

@login_required
def gerenciar_administrador(request):
  erro = False
  if request.user.groups.filter(name="administradores").exists():
    return render(request, 'colaborador/gerenciar.html')
  erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/administrador.html', context)


