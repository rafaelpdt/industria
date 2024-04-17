# Generated by Django 5.0.4 on 2024-04-17 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bairro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cargo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_imovel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLogradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_logadouro', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcionario', models.CharField(max_length=100)),
                ('cpf_func', models.CharField(max_length=11)),
                ('data_nasc_func', models.DateField(max_length=8)),
                ('email_func', models.CharField(max_length=100)),
                ('salario', models.CharField(max_length=8)),
                ('nome_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargos')),
            ],
        ),
        migrations.CreateModel(
            name='Logradouro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=4)),
                ('complemento', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('nome_bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bairro')),
                ('tipo_logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipologradouro')),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_imovel', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=500)),
                ('area_contruida', models.CharField(max_length=10)),
                ('numero_comodos', models.CharField(max_length=2)),
                ('cor', models.CharField(max_length=30)),
                ('vagas_garagem', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
                ('nome_bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.bairro')),
                ('nome_logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.logradouro')),
                ('tipo_imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoimovel')),
                ('tipo_logradouro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipologradouro')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uf')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=8)),
                ('data_nasc', models.DateField(max_length=8)),
                ('email', models.CharField(max_length=100)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Locatorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoas')),
            ],
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_aluguel', models.CharField(max_length=5)),
                ('nome_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('nome_imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.imovel')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoas')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uf'),
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_venda', models.CharField(max_length=9)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoas')),
                ('nome_funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('nome_imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.imovel')),
            ],
        ),
    ]