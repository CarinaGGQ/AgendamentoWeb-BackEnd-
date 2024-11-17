from django.shortcuts import render

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
