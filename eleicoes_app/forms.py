from django import forms
from .models import Candidato, Cargo, Eleicao, Chapa, CandidatoChapa, Eleitor

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'cpf', 'endereco']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['cargo', 'eleicao']

class EleicaoForm(forms.ModelForm):
    class Meta:
        model = Eleicao
        fields = ['data_eleicao', 'local_eleicao', 'hora_inicial', 'hora_final']

class ChapaForm(forms.ModelForm):
    class Meta:
        model = Chapa
        fields = ['nome_chapa', 'eleicao']

class CandidatoChapaForm(forms.ModelForm):
    class Meta:
        model = CandidatoChapa
        fields = ['chapa', 'cargo', 'candidato']

class EleitorForm(forms.ModelForm):
    class Meta:
        model = Eleitor
        fields = ['nome', 'cpf', 'endereco', 'senha']
