from django.urls import include, path
from django.contrib import admin
from eleicoes_app import admin
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listar_liberacoes/', views.listar_liberacoes, name='listar_liberacoes'),
    path('liberar_eleitor/', views.liberar_eleitor, name='liberar_eleitor'),
    path('candidatos/', views.cadastrar_candidato, name='cadastrar_candidato'),
    path('lista/', views.lista_candidatos, name='lista_candidatos'),
    path('lista_cargos/', views.lista_cargos, name='lista_cargos'),
    path('lista_eleicoes/', views.lista_eleicoes, name='lista_eleicoes'),
    path('lista_chapas/', views.lista_chapas, name='lista_chapas'),
    path('lista_candidatos_chapa/', views.lista_candidatos_chapa, name='lista_candidatos_chapa'),
    path('lista_eleitores/', views.lista_eleitores, name='lista_eleitores'),
    path('cargos/', views.cadastrar_cargo, name='cadastrar_cargo'),
    path('eleicoes/', views.cadastrar_eleicao, name='cadastrar_eleicao'),
    path('chapas/', views.cadastrar_chapa, name='cadastrar_chapa'),
    path('candidatos_chapa/', views.cadastrar_candidato_chapa, name='cadastrar_candidato_chapa'),
    path('eleitores/', views.cadastrar_eleitor, name='cadastrar_eleitor'),
    path('iniciar_votacao/', views.iniciar_votacao, name='iniciar_votacao'),
    path('gerar_relatorio_inicializacao/', views.gerar_relatorio_inicializacao, name='gerar_relatorio_inicializacao'),
    path('votar/', views.votar, name='votar'),
    path('encerrar_votacao/', views.encerrar_votacao, name='encerrar_votacao'),
    path('gerar_relatorio_fechamento/', views.gerar_relatorio_fechamento, name='gerar_relatorio_fechamento'),
    path('confirmar_voto/', views.confirmar_voto, name='confirmar_voto'),
    path('listar_locais/', views.listar_locais, name='listar_locais'),
]
