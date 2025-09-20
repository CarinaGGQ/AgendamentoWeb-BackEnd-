from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from .models import Cliente, Serviço, AgendamentoDisponivel, Agendamento, Feedback, LISTA_HORARIOS
from datetime import datetime


def homepage(request):
    return render(request, 'homepage.html')


def feedback(request):
    servicos = Serviço.objects.filter(ativo=True)

    if request.method == 'POST':
        nome_cliente = request.POST.get('name')
        email_cliente = request.POST.get('email')
        servico_id = request.POST.get('servico')
        feedback_text = request.POST.get('feedback')

        if nome_cliente and email_cliente and servico_id and feedback_text:
            cliente, _ = Cliente.objects.get_or_create(
                email=email_cliente,
                defaults={'nome': nome_cliente}
            )
            servico = get_object_or_404(Serviço, id=servico_id)

            Feedback.objects.create(
                cliente=cliente,
                serviço=servico,
                feedback=feedback_text
            )

            return render(request, 'feedback_sucesso.html', {
                'cliente': cliente,
                'servico': servico,
                'feedback': feedback_text
            })

    return render(request, 'feedback.html', {'servicos': servicos})


def feedback_sucesso(request):
    return render(request, 'feedback_sucesso.html')


# ------------------- AGENDAMENTO -------------------

def horarios_disponiveis(request):
    data = request.GET.get("data")
    if not data:
        return JsonResponse({"error": "Data não fornecida"}, status=400)

    horarios_validos = [h[0] for h in LISTA_HORARIOS]
    ocupados = AgendamentoDisponivel.objects.filter(dia=data).values_list("hora", flat=True)

    disponiveis = [h for h in horarios_validos if h not in ocupados]

    horarios_label = dict(LISTA_HORARIOS)
    response = [{"hora": h, "label": horarios_label[h]} for h in disponiveis]

    return JsonResponse(response, safe=False)

def agendamento(request):
    # Buscar apenas horários que NÃO estão associados a agendamentos
    agendamentos_ocupados = Agendamento.objects.values_list('agendamento_disponivel_id', flat=True)
    horarios_disponiveis = AgendamentoDisponivel.objects.exclude(id__in=agendamentos_ocupados)

    servicos = Serviço.objects.filter(ativo=True)

    return render(request, 'agendamento.html', {
        'servicos': servicos,
        'horarios_disponiveis': horarios_disponiveis
    })


def confirmacao(request):
    if request.method == "POST":
        nome = request.POST.get("name")
        email = request.POST.get("email")
        servico_id = request.POST.get("servico")
        selected_date = request.POST.get("selected_date")
        selected_time = request.POST.get("selected_time")

        # Cliente
        cliente, _ = Cliente.objects.get_or_create(nome=nome, email=email)

        # Serviço
        servico = Serviço.objects.get(id=servico_id)

        # Agenda disponível
        agendamento_disp, _ = AgendamentoDisponivel.objects.get_or_create(
            dia=selected_date,
            hora=selected_time
        )

        # Criar o agendamento
        Agendamento.objects.create(
            cliente=cliente,
            serviço=servico,
            agendamento_disponivel=agendamento_disp,
            finalizado=True
        )

        # Formatar data para exibir
        formatted_date = datetime.strptime(selected_date, "%Y-%m-%d").strftime("%d/%m/%Y")

        # Redirecionar para página de sucesso com contexto
        return render(request, "confirmacao_sucesso.html", {
            "data": formatted_date,
            "hora": selected_time,
            "servico": servico.nome
        })

    else:
        selected_date = request.GET.get("selected_date")
        selected_time = request.GET.get("selected_time")
        formatted_date = datetime.strptime(selected_date, "%Y-%m-%d").strftime("%d/%m/%Y")

        return render(request, "confirmacao.html", {
            "selected_date": selected_date,
            "formatted_date": formatted_date,
            "selected_time": selected_time,
            "servicos": Serviço.objects.filter(ativo=True),
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


# ------------------- LOGIN E PAINÉIS -------------------

def aluno(request):
    erro = False
    mensagem = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        usuario = authenticate(request, username=username, password=password)

        if usuario:
            if usuario.groups.filter(name="Alunos").exists():
                login(request, usuario)
                return redirect('gerenciar_aluno')
            else:
                mensagem = "Você não tem permissão para acessar como Aluno."
                erro = True
        else:
            mensagem = "Credenciais inválidas."
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
            if usuario.groups.filter(name="Professores").exists():
                login(request, usuario)
                return redirect('gerenciar_professor')
            else:
                mensagem = "Você não tem permissão para acessar como Professor."
                erro = True
        else:
            mensagem = "Credenciais inválidas."
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
            if usuario.groups.filter(name="Administradores").exists():
                login(request, usuario)
                return redirect('gerenciar_administrador')
            else:
                mensagem = "Você não tem permissão para acessar como Administrador."
                erro = True
        else:
            mensagem = "Credenciais inválidas."
            erro = True

    return render(request, 'colaborador/administrador.html', {"erro": erro, "mensagem": mensagem})


@login_required
def gerenciar_aluno(request):
    if request.user.groups.filter(name="Alunos").exists():
        agendamentos = Agendamento.objects.all()
        feedbacks = Feedback.objects.all()
        return render(request, 'colaborador/gerenciar_aluno.html', {'agendamentos': agendamentos, 'feedbacks': feedbacks})
    return render(request, 'colaborador/aluno.html', {"erro": True})


@login_required
def gerenciar_professor(request):
    if request.user.groups.filter(name="Professores").exists():
        agendamentos = Agendamento.objects.all()
        feedbacks = Feedback.objects.all()
        return render(request, 'colaborador/gerenciar_professor.html', {'agendamentos': agendamentos, 'feedbacks': feedbacks})
    return render(request, 'colaborador/professor.html', {"erro": True})


@login_required
def gerenciar_administrador(request):
    if request.user.groups.filter(name="Administradores").exists():
        agendamentos = Agendamento.objects.all()
        feedbacks = Feedback.objects.all()
        return render(request, 'colaborador/gerenciar_administrador.html', {'agendamentos': agendamentos, 'feedbacks': feedbacks})
    return render(request, 'colaborador/administrador.html', {"erro": True})


# ------------------- EVENTOS -------------------

def eventos(request):
    agendamentos = Agendamento.objects.all()
    eventos = [
        {
            "title": agendamento.titulo,
            "start": agendamento.inicio.isoformat(),
            "end": agendamento.fim.isoformat(),
            "date": agendamento.inicio.date().isoformat(),
            "time": agendamento.inicio.strftime("%H:%M"),
        }
        for agendamento in agendamentos
    ]
    return JsonResponse(eventos, safe=False)
