from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest
from .models import LiberacaoEleitor, Eleicao, Candidato, Cargo, Chapa, CandidatoChapa, Eleitor, Voto
from .forms import CandidatoForm, CargoForm, EleicaoForm, ChapaForm, CandidatoChapaForm, EleitorForm

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect(reverse('pagina_inicial'))
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def logout(request):
#     auth_logout(request)
#     return redirect(reverse('pagina_inicial'))

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')


def cadastrar_candidato(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_candidatos'))
    else:
        form = CandidatoForm()
    return render(request, 'cadastrar_candidato.html', {'form': form})

def cadastrar_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_cargos'))
    else:
        form = CargoForm()
    return render(request, 'cadastrar_cargo.html', {'form': form})

def cadastrar_eleicao(request):
    if request.method == 'POST':
        form = EleicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_eleicoes'))
    else:
        form = EleicaoForm()
    return render(request, 'cadastrar_eleicao.html', {'form': form})

def cadastrar_chapa(request):
    if request.method == 'POST':
        form = ChapaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_chapas'))
    else:
        form = ChapaForm()
    return render(request, 'cadastrar_chapa.html', {'form': form})

def cadastrar_candidato_chapa(request):
    if request.method == 'POST':
        form = CandidatoChapaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_candidatos_chapa'))
    else:
        form = CandidatoChapaForm()
    return render(request, 'cadastrar_candidato_chapa.html', {'form': form})

def cadastrar_eleitor(request):
    if request.method == 'POST':
        form = EleitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_eleitores'))
    else:
        form = EleitorForm()
    return render(request, 'cadastrar_eleitor.html', {'form': form})

def iniciar_votacao(request):
    if request.method == 'POST':
        eleicao_id = request.POST.get('eleicao_id')
        eleicao = Eleicao.objects.get(id=eleicao_id)
        eleicao.ativa = True
        eleicao.save()
        return redirect(reverse('listar_locais'))
    eleicoes = Eleicao.objects.all()
    return render(request, 'iniciar_votacao.html', {'eleicoes': eleicoes})

def votar(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        eleicao_id = request.POST.get('eleicao_id')
        candidato_id = request.POST.get('candidato_id')
        
        try:
            eleitor = Eleitor.objects.get(cpf=cpf, senha=senha)
        except Eleitor.DoesNotExist:
            return HttpResponseBadRequest("Eleitor não encontrado ou senha incorreta.")
        
        try:
            eleicao = Eleicao.objects.get(id=eleicao_id, ativa=True)
        except Eleicao.DoesNotExist:
            return HttpResponseBadRequest("Eleição não encontrada ou não está ativa.")
        
        # Verifica se o eleitor já votou nesta eleição
        if Voto.objects.filter(eleicao=eleicao, eleitor=eleitor).exists():
            return HttpResponseBadRequest("Este eleitor já votou nesta eleição.")
        
        try:
            candidato = Candidato.objects.get(id=candidato_id)
        except Candidato.DoesNotExist:
            return HttpResponseBadRequest("Candidato não encontrado.")

        novo_voto = Voto.objects.create(eleicao=eleicao, eleitor=eleitor, candidato=candidato)
        
        if candidato:
            candidato.numero_votos += 1
            candidato.save()

        return redirect(reverse('confirmar_voto'))

    eleicoes = Eleicao.objects.filter(ativa=True)
    candidatos = Candidato.objects.all()
    return render(request, 'votar.html', {'eleicoes': eleicoes, 'candidatos': candidatos})

def encerrar_votacao(request):
    if request.method == 'POST':
        eleicao_id = request.POST.get('eleicao_id')
        eleicao = Eleicao.objects.get(id=eleicao_id)
        eleicao.ativa = False
        eleicao.save()
        return redirect(reverse('listar_locais'))
    eleicoes = Eleicao.objects.all()
    return render(request, 'encerrar_votacao.html', {'eleicoes': eleicoes})

def liberar_eleitor(request):
    if request.method == 'POST':
        cpf_eleitor = request.POST.get('cpf_eleitor')
        eleicao_id = request.POST.get('eleicao_id')
        data_hora_inicio_str = request.POST.get('data_hora_inicio')

        # Converter a string para um objeto datetime
        try:
            data_hora_inicio = datetime.strptime(data_hora_inicio_str, '%Y-%m-%dT%H:%M')
        except ValueError:
            return HttpResponseBadRequest('Formato de data inválido')

        # Verificar se a eleição existe
        try:
            eleicao = Eleicao.objects.get(id=eleicao_id)
        except Eleicao.DoesNotExist:
            return HttpResponseBadRequest('Eleição não encontrada')

        # Criar a instância de LiberacaoEleitor
        liberacao = LiberacaoEleitor.objects.create(
            cpf_eleitor=cpf_eleitor,
            status_liberacao=True,
            eleicao=eleicao,
            usuario_liberacao=request.user,  # Utilizando o usuário atual
            data_hora_inicio=make_aware(data_hora_inicio)  # Garante que o datetime tenha informação de fuso horário
        )

        return redirect(reverse('listar_liberacoes'))

    # Se o método não for POST, renderizar o formulário com as eleições disponíveis
    eleicoes = Eleicao.objects.all()
    return render(request, 'liberar_eleitor.html', {'eleicoes': eleicoes})


def listar_liberacoes(request):
    liberacoes = LiberacaoEleitor.objects.all()
    return render(request, 'listar_liberacoes.html', {'liberacoes': liberacoes})

####

def gerar_relatorio_inicializacao(request):
    if request.method == 'POST':
        # Implementar lógica para gerar relatório
        return redirect(reverse('lista_relatorios'))
    return render(request, 'gerar_relatorio_inicializacao.html')

def gerar_relatorio_fechamento(request):
    if request.method == 'POST':
        # Implementar lógica para gerar relatório
        return redirect(reverse('lista_relatorios'))
    return render(request, 'gerar_relatorio_fechamento.html')

####
def lista_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'lista_candidatos.html', {'candidatos': candidatos})

def lista_cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'lista_cargos.html', {'cargos': cargos})

def lista_eleicoes(request):
    eleicoes = Eleicao.objects.all()
    return render(request, 'lista_eleicoes.html', {'eleicoes': eleicoes})

def lista_chapas(request):
    chapas = Chapa.objects.all()
    return render(request, 'lista_chapas.html', {'chapas': chapas})

def lista_candidatos_chapa(request):
    candidatos_chapa = CandidatoChapa.objects.all()
    return render(request, 'lista_candidatos_chapa.html', {'candidatos_chapa': candidatos_chapa})

def lista_eleitores(request):
    eleitores = Eleitor.objects.all()
    return render(request, 'lista_eleitores.html', {'eleitores': eleitores})

def listar_locais(request):
    eleicoes_ativas = Eleicao.objects.filter(ativa=True)
    eleicoes_inativas = Eleicao.objects.filter(ativa=False)
    context = {
        'eleicoes_ativas': eleicoes_ativas,
        'eleicoes_inativas': eleicoes_inativas,
    }
    return render(request, 'listar_locais.html', context)

def confirmar_voto(request):
    ultimo_voto = Voto.objects.latest('id')  # Obtém o último voto registrado
    return render(request, 'confirmar_voto.html', {'voto': ultimo_voto})