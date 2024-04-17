"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('uf/',UfView.as_view(), name='uf'),
    path('cidade/',CidadeView.as_view(), name='cidades'),
    path('pessoa/',PessoaView.as_view(), name='pessoa'),
    path('cargo/',CargoView.as_view(), name='cargos'),
    path('funcionario/',FuncionarioView.as_view(), name='funcionarios'),
    path('tipo_logradouro/',TipoLogradouroView.as_view(), name='tipo_logradouros'),
    path('bairro/',BairroView.as_view(), name='bairros'),
    path('logradouro/',LogradouroView.as_view(), name='logradouros'),
    path('tipo_imovel/',TipoImovelView.as_view(), name='tipo_imoveis'),
    path('imovel/',ImovelView.as_view(), name='imoveis'),
    path('locacao/',LocacaoView.as_view(), name='locacaos'),
    path('venda/',VendaView.as_view(), name='vendas'),
]
