from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from basiM7S1.models import CadastroCliente
import requests


@api_view()
def Cliente(requests):
   
    resposta = CadastroCliente.objects.all()
    dados =[]
    for cadastro in resposta:
        dado =  {
            'nome':cadastro.nome,
            'idade':cadastro.idade,
            'telefone':cadastro.telefone,
            'status': cadastro.status,
        }             
        dados.append(dado)
    return Response(dados)

@api_view(http_method_names=['POST'])
def CadastrandoCliente(requests):
    nome = requests.data['nome']
    idade = requests.data['idade']
    telefone = requests.data['telefone']
    status = requests.data['status']
    cadastro = CadastroCliente.objects.create(nome=nome,idade=idade,telefone=telefone,status=status)
    dados = {
        'id': cadastro.id,
        'nome':cadastro.nome,
        'idade':cadastro.idade,
        'telefone':cadastro.telefone,
        'status': cadastro.status,
    }
    return Response(dados)




