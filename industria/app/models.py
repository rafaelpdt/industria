from django.db import models

class Uf(models.Model):
    uf = models.CharField(max_length=2)
    def __str__(self):
        return self.uf

class Cidade(models.Model):
    cidade = models.CharField(max_length=100)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.cidade}, {self.uf}"

class TipoLogradouro(models.Model):
    tipo_logradouro = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo_logradouro
    
class Bairro(models.Model):
    nome_bairro = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_bairro

class Logradouro(models.Model):
    tipo_logradouro = models.ForeignKey(TipoLogradouro, on_delete=models.CASCADE)
    nome_logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=4)
    complemento = models.CharField(max_length=100)
    nome_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    def __str__(self):
        return f"{self.tipo_logradouro},{self.nome_logradouro},{self.nome_bairro}"
    
class Cargos(models.Model):
    nome_cargo = models.CharField(max_length=30)
    def __str__(self):
        return self.nome_cargo

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)
    nome_cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    cpf_func = models.CharField(max_length=11)
    data_nasc_func = models.DateField(max_length=8)
    email_func = models.CharField(max_length=100)
    salario = models.CharField(max_length=8)
    def __str__(self):
        return f"{self.nome_funcionario},{self.nome_cargo}"

    
class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    data_nasc = models.DateField(max_length=8)
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class TipoImovel(models.Model):
    tipo_imovel = models.CharField(max_length=30)
    def __str__(self):
        return self.tipo_imovel

class Imovel(models.Model):
    nome_imovel = models.CharField(max_length=100)
    tipo_imovel = models.ForeignKey(TipoImovel, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500)
    area_contruida = models.CharField(max_length=10)
    numero_comodos = models.CharField(max_length=2)
    cor = models.CharField(max_length=30)
    vagas_garagem = models.CharField(max_length=2)
    tipo_logradouro = models.ForeignKey(TipoLogradouro, on_delete=models.CASCADE)
    nome_bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    def __str__(self):
        return f"{self.nome_imovel}, {self.tipo_imovel}"
   
class Vendas(models.Model):
    nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    nome_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome_imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    valor_venda = models.CharField(max_length=9)
    def __str__(self):
        return f"{self.nome}, {self.nome_imovel}, {self.valor_venda}"
    
class Locacao(models.Model):
    nome = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    nome_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome_imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    valor_aluguel = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.nome}, {self.nome_imovel}, {self.valor_aluguel}"
    
