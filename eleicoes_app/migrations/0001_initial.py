# Generated by Django 4.1.7 on 2024-06-09 00:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('endereco', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Eleicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_eleicao', models.DateField()),
                ('local_eleicao', models.CharField(max_length=255)),
                ('hora_inicial', models.TimeField()),
                ('hora_final', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Eleitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('endereco', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_votos', models.IntegerField(default=0)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.candidato')),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='RelatorioInicializacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista_candidatos_votos', models.JSONField()),
                ('total_eleitores', models.IntegerField()),
                ('arquivo_pdf', models.FileField(upload_to='relatorios/')),
                ('data_hora_abertura', models.DateTimeField()),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='RelatorioFechamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista_candidatos_votos', models.JSONField()),
                ('total_eleitores_votaram', models.IntegerField()),
                ('arquivo_pdf', models.FileField(upload_to='relatorios/')),
                ('data_hora_fechamento', models.DateTimeField()),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='LiberacaoEleitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_eleitor', models.CharField(max_length=11)),
                ('status_liberacao', models.BooleanField(default=False)),
                ('data_hora_inicio', models.DateTimeField()),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.eleicao')),
                ('usuario_liberacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_chapa', models.CharField(max_length=255)),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=255)),
                ('eleicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.eleicao')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatoChapa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.candidato')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.cargo')),
                ('chapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eleicoes_app.chapa')),
            ],
        ),
    ]