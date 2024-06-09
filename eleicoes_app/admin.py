from django.contrib import admin
from .models import Eleicao, Candidato, Cargo, Chapa, CandidatoChapa, Eleitor, RelatorioInicializacao, LiberacaoEleitor, Voto, RelatorioFechamento

admin.site.register(Eleicao)
admin.site.register(Candidato)
admin.site.register(Cargo)
admin.site.register(Chapa)
admin.site.register(CandidatoChapa)
admin.site.register(Eleitor)
admin.site.register(RelatorioInicializacao)
admin.site.register(LiberacaoEleitor)
admin.site.register(Voto)
admin.site.register(RelatorioFechamento)
