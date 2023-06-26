import json
from .saldo import *
from .estoque import *

def adicionaPreferencia(nomejogo, path):
    if type(nomeJogo) != str:
        return 1
    data={"tipo":"preferencia-novo-jogo", "dados": {"nome": nomejogo, "preco": 5, "fabricante": "Microny"}}
    path = path + nomejogo
    with open(path , "w") as arq:
        json.dump(data,arq,indent=4) 
    return 0

def compraJogo(nomejogo, pathval, pathpref):
    if type(nomeJogo) != str:
        return 1
    preco = recebePrecoCompra(nomejogo, pathval)
    if preco < 0:
        adicionaPreferencia(nomejogo, pathpref)
        return 3
    if verificaSaldo()>=preco:
        removeSaldo(preco)
        AdicionaEstoqueTotal(nomejogo)
        return 0
    else:
        adicionaPreferencia(nomejogo, pathpref)
        return 2
    return

def recebePrecoCompra(nomejogo, path):
    if type(nomeJogo) != str:
        return 0
    with open(path, 'r') as arq:
        dados_json = json.load(arq)
        for el in range(len(dados_json)):
            if nomejogo== dados_json[el]["nome"]: ##jogo existe e está nessa linha 
                preco = dados_json[el]["preco"]
                return preco
        ##nao existe o nomejogo no arquivo
    return -1
