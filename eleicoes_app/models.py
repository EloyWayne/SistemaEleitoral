from django.db import models

from django.db import models
from django.contrib.auth.models import User

# RF03 - Cadastro de Eleições
class Eleicao(models.Model):
    data_eleicao = models.DateField()
    local_eleicao = models.CharField(max_length=255)
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    ativa = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.local_eleicao} - {self.data_eleicao}"

# RF01 - Cadastro de Candidatos
class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=255)
    numero_votos = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

# RF02 - Cadastro de Cargos
class Cargo(models.Model):
    cargo = models.CharField(max_length=255)
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.cargo

# RF04 - Cadastro de Chapas
class Chapa(models.Model):
    nome_chapa = models.CharField(max_length=255)
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_chapa

# RF05 - Cadastro de Candidatos nas Chapas
class CandidatoChapa(models.Model):
    chapa = models.ForeignKey(Chapa, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidato} - {self.cargo} ({self.chapa})"

# RF06 - Cadastro de Eleitores
class Eleitor(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

# RF07 - Relatório de Inicialização da Eleição
class RelatorioInicializacao(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    lista_candidatos_votos = models.JSONField()
    total_eleitores = models.IntegerField()
    arquivo_pdf = models.FileField(upload_to='relatorios/')
    data_hora_abertura = models.DateTimeField()

    def __str__(self):
        return f"Relatório Inicialização - {self.eleicao}"

# RF08 - Liberação de Eleitor para Votação
class LiberacaoEleitor(models.Model):
    cpf_eleitor = models.CharField(max_length=11)
    status_liberacao = models.BooleanField(default=False)
    data_hora_inicio = models.DateTimeField()
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    usuario_liberacao = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Liberacao - {self.cpf_eleitor} - {self.eleicao}"

# RF09 - Cadastro de Votos
class Voto(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    eleitor = models.ForeignKey(Eleitor, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    numero_votos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.eleitor} - {self.eleicao} - {self.candidato}"

# RF10 - Relatório de Fechamento da Eleição
class RelatorioFechamento(models.Model):
    eleicao = models.ForeignKey(Eleicao, on_delete=models.CASCADE)
    lista_candidatos_votos = models.JSONField()
    total_eleitores_votaram = models.IntegerField()
    arquivo_pdf = models.FileField(upload_to='relatorios/')
    data_hora_fechamento = models.DateTimeField()

    def __str__(self):
        return f"Relatório Fechamento - {self.eleicao}"
