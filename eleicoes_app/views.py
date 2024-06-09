from django.shortcuts import render, redirect
from django.urls import reverse

from eleicoes_app.models import Candidato, CandidatoChapa, Cargo, Chapa, Eleicao, Eleitor
from .forms import (
    CandidatoForm, CargoForm, EleicaoForm, ChapaForm, 
    CandidatoChapaForm, EleitorForm
)

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

#####

def iniciar_votacao(request):
    if request.method == 'POST':
        # Logic to start voting process
        return redirect(reverse('lista_eleicoes'))
    return render(request, 'iniciar_votacao.html')

def gerar_relatorio_inicializacao(request):
    if request.method == 'POST':
        # Logic to generate initialization report
        return redirect(reverse('lista_relatorios'))
    return render(request, 'gerar_relatorio_inicializacao.html')

def votar(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        # Logic to handle voting process
        return redirect(reverse('confirmar_voto'))
    return render(request, 'votar.html')

def encerrar_votacao(request):
    if request.method == 'POST':
        # Logic to end voting process
        return redirect(reverse('lista_eleicoes'))
    return render(request, 'encerrar_votacao.html')

def gerar_relatorio_fechamento(request):
    if request.method == 'POST':
        # Logic to generate closing report
        return redirect(reverse('lista_relatorios'))
    return render(request, 'gerar_relatorio_fechamento.html')
#####

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