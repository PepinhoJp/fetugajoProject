import json
from .saldo import *
from .estoque import *
from time import time

def adicionaPreferencia(nomejogo, path):
    if type(nomejogo) != str:
        return 1
    data={"tipo":"preferencia-novo-jogo", "dados": {"nome": nomejogo, "preco": 5, "fabricante": "Microny"}}
    path = path + nomejogo + ".json"
    with open(path , "w") as arq:
        json.dump(data,arq,indent=4)
    return 0

def compraJogo(nomejogo, pathtabela, pathmsg):
    if type(nomejogo) != str:
        return 1
    preco = recebePrecoCompra(nomejogo, pathtabela)
    if preco < 0:
        adicionaPreferencia(nomejogo, pathmsg)
        return 3
    if verificaSaldo()>=preco:
        removeSaldo(preco)
        adicionaEstoqueTotal(nomejogo, 1)
        data={"tipo":"venda-jogo", "dados": nomejogo}
        path = pathmsg + nomejogo + str(int(time())) + ".json"
        with open(path, "w") as arq:
            json.dump(data,arq, indent = 4)
        return 0
    else:
        adicionaPreferencia(nomejogo, pathmsg)
        return 2
    return

def recebePrecoCompra(nomejogo, path):
    if type(nomejogo) != str:
        return 0
    with open(path, 'r') as arq:
        dados_json = json.load(arq)
        for el in range(len(dados_json)):
            if nomejogo== dados_json[el]["nome"]: ##jogo existe e está nessa linha
                preco = dados_json[el]["preco"]
                return preco
        ##nao existe o nomejogo no arquivo
    return -1