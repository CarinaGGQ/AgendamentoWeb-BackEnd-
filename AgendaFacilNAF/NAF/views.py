from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Cliente, Serviço, AgendamentoDisponivel, Agendamento
from datetime import datetime

def homepage(request):
  return render(request, 'homepage.html')

def feedback(request):
  return render(request, 'feedback.html')

def agendamento(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date', '')
        selected_time = request.POST.get('selected_time', '')

        # Redireciona para a página de confirmação com os dados
        return redirect(f"{reverse('confirmacao')}?selected_date={selected_date}&selected_time={selected_time}")

    return render(request, 'agendamento.html')

def confirmacao(request):
    # Buscar dados de data e hora da URL (GET)
    selected_date = request.GET.get('selected_date', '')
    selected_time = request.GET.get('selected_time', '')

    # Corrigir o formato da data, se necessário
    try:
        if selected_date:
            # Converte de DD/MM/YYYY para YYYY-MM-DD
            selected_date = datetime.strptime(selected_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        # Caso o formato esteja incorreto, pode lançar um erro personalizado
        return HttpResponse("Formato de data inválido.", status=400)

    # Buscar todos os serviços ativos
    servicos = Serviço.objects.filter(ativo=True)

    if request.method == 'POST':
        # Obter dados enviados via formulário
        nome_cliente = request.POST.get('name')
        email_cliente = request.POST.get('email')
        servico_id = request.POST.get('servico')

        if nome_cliente and email_cliente and selected_date and selected_time and servico_id:
            # Buscar ou criar o cliente
            cliente, _ = Cliente.objects.get_or_create(
                email=email_cliente,
                defaults={'nome': nome_cliente}
            )
            # Obter o serviço selecionado
            servico = get_object_or_404(Serviço, id=servico_id)
            # Criar ou obter agendamento disponível
            agendamento_disponivel, _ = AgendamentoDisponivel.objects.get_or_create(
                dia=selected_date,
                hora=selected_time
            )

            # Criar o agendamento
            Agendamento.objects.create(
                cliente=cliente,
                serviço=servico,
                AgendamentoDisponivel=agendamento_disponivel,
                finalizado=False
            )

            redirect_url = f"{reverse('confirmacao_sucesso')}?servico={servico.nome}&data={selected_date}&hora={selected_time}"
            return redirect(redirect_url)

    # Renderizar a página de confirmação com os dados e serviços
    return render(request, 'confirmacao.html', {
        'selected_date': selected_date,
        'selected_time': selected_time,
        'servicos': servicos,
    })

def confirmacao_sucesso(request):
    servico = request.GET.get('servico', '')
    data = request.GET.get('data', '')
    hora = request.GET.get('hora', '')

    return render(request, 'confirmacao_sucesso.html', {
        'servico': servico,
        'data': data,
        'hora': hora,
    })

def aluno(request):
  erro = False
  mensagem = ""

  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    usuario = authenticate(request, username=username, password=password)

    if usuario:
      # Verifica se o usuário pertence ao grupo "Alunos"
      if usuario.groups.filter(name="Alunos").exists():
        login(request, usuario)
        return redirect('gerenciar_aluno')  # Redireciona para a página gerenciada pelo grupo
      else:
        mensagem = "Você não tem permissão para acessar como Aluno."
        erro = True
    else:
      mensagem = "Credenciais inválidas. Verifique o nome de usuário e senha."
      erro = True

  return render(request, 'colaborador/aluno.html', {"erro": erro, "mensagem": mensagem})


def professor(request):
  erro = False
  mensagem = ""

  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    usuario = authenticate(request, username=username, password=password)

    if usuario:
      # Verifica se o usuário pertence ao grupo "Professores"
      if usuario.groups.filter(name="Professores").exists():
        login(request, usuario)
        return redirect('gerenciar_professor')  # Redireciona para a página gerenciada pelo grupo
      else:
        mensagem = "Você não tem permissão para acessar como Professor."
        erro = True
    else:
      mensagem = "Credenciais inválidas. Verifique o nome de usuário e senha."
      erro = True

  return render(request, 'colaborador/professor.html', {"erro": erro, "mensagem": mensagem})


def administrador(request):
  erro = False
  mensagem = ""

  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    usuario = authenticate(request, username=username, password=password)

    if usuario:
      # Verifica se o usuário pertence ao grupo "Administradores"
      if usuario.groups.filter(name="Administradores").exists():
        login(request, usuario)
        return redirect('gerenciar_administrador')  # Redireciona para a página gerenciada pelo grupo
      else:
        mensagem = "Você não tem permissão para acessar como Administrador."
        erro = True
    else:
      mensagem = "Credenciais inválidas. Verifique o nome de usuário e senha."
      erro = True

  return render(request, 'colaborador/administrador.html', {"erro": erro, "mensagem": mensagem})


@login_required
def gerenciar_aluno(request):
  erro = False
  if request.user.groups.filter(name="Alunos").exists():
    return render(request, 'colaborador/gerenciar_aluno.html')
  else:
    erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/aluno.html', context)


@login_required
def gerenciar_professor(request):
  erro = False
  if request.user.groups.filter(name="Professores").exists():
    return render(request, 'colaborador/gerenciar_professor.html')
  else:
    erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/professor.html', context)


@login_required
def gerenciar_administrador(request):
  erro = False
  if request.user.groups.filter(name="Administradores").exists():
    return render(request, 'colaborador/gerenciar_administrador.html')
  else:
    erro = True
  context = {"erro": erro}
  return render(request, 'colaborador/administrador.html', context)
