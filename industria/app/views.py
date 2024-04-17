from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'index.html')
    def post(self, request):
        pass

class UfView(View):
    def get(self, request, *args, **kwargs):
        uf = Uf.objects.all()
        return render(request,'uf.html',{'uf': uf})

class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request,'cidade.html',{'cidade': cidades})

class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoas.objects.all()
        return render(request,'pessoa.html',{'pessoa': pessoas})

class CargoView(View):
    def get(self, request, *args, **kwargs):
        cargos = Cargos.objects.all()
        return render(request,'cargo.html',{'cargo': cargos})

class FuncionarioView(View):
    def get(self, request, *args, **kwargs):
        funcionarios = Funcionario.objects.all()
        return render(request,'funcionario.html',{'funcionario': funcionarios})

class TipoLogradouroView(View):
    def get(self, request, *args, **kwargs):
        tipo_logradouros = TipoLogradouro.objects.all()
        return render(request,'tipo_logradouro.html',{'tipo_logradouro': tipo_logradouros})

class BairroView(View):
    def get(self, request, *args, **kwargs):
        bairros = Bairro.objects.all()
        return render(request,'bairro.html',{'bairro': bairros})

class LogradouroView(View):
    def get(self, request, *args, **kwargs):
        logradouros = Logradouro.objects.all()
        return render(request,'logradouro.html',{'logradouro': logradouros})

class TipoImovelView(View):
    def get(self, request, *args, **kwargs):
        tipo_imoveis = TipoImovel.objects.all()
        return render(request,'tipo_imovel.html',{'tipo_imovel': tipo_imoveis})

class ImovelView(View):
    def get(self, request, *args, **kwargs):
        imoveis = Imovel.objects.all()
        return render(request,'imovel.html',{'imovel': imoveis})

class LocacaoView(View):
    def get(self, request, *args, **kwargs):
        locacaos = Locacao.objects.all()
        return render(request,'locacao.html',{'locacao': locacaos})

class VendaView(View):
    def get(self, request, *args, **kwargs):
        vendas = Vendas.objects.all()
        return render(request,'venda.html',{'venda': vendas})
