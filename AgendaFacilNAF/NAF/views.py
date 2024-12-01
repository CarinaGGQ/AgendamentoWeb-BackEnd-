from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def homepage(request):
  return render(request, 'homepage.html')

def feedback(request):
  return render(request, 'feedback.html')

def agendamento(request):
    if request.method == 'POST':
      selected_date = request.POST.get('selected_date', '')
      selected_time = request.POST.get('selected_time', '')

      # Renderiza a página de confirmação com os dados selecionados
      return render(request, 'confirmacao.html', {
        'selected_date': selected_date,
        'selected_time': selected_time
      })

    return render(request, 'agendamento.html')

def confirmacao(request):
    # Os valores serão passados pela requisição POST
    selected_date = request.POST.get('selected_date', '')
    selected_time = request.POST.get('selected_time', '')

    return render(request, 'confirmacao.html', {
        'selected_date': selected_date,
        'selected_time': selected_time
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
