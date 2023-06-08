from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .modulos.saldo import *
from .modulos.estoque import *

import os

#Saldo empresa
script_dir = os.path.dirname(__file__)
rel_path = "../data/saldo.json"
abs_file_path = os.path.join(script_dir, rel_path)

#Estoque jogo
script_dir = os.path.dirname(__file__)
rel_path = "../data/estoqueAluguel.json"
abs_file_path2 = os.path.join(script_dir, rel_path)

def index(request):
    removeSaldo(abs_file_path, 500.23)
    adicionaEstoqueAluguel(abs_file_path2, "TLOU 2", 20)
    return HttpResponse("Hello, world. You're at the polls index. " + str(verificaSaldo(abs_file_path)) + str(buscaNoEstoque(abs_file_path2, "Super Mario")))