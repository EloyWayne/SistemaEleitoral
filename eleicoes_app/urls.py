from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'), 
    path('candidatos/', views.cadastrar_candidato, name='cadastrar_candidato'),
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
]
