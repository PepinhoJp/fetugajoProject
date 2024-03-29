import json
from .estoque import *
from .cliente import *
from .saldo import *
from .compra import *
import os
import time


def validaAluguel(f):
    def valida(nomeJogo, nomeCliente):
        if verificaCliente(nomeCliente):
            return f(nomeJogo, nomeCliente)
        return 2

    return valida


@validaAluguel
def alugaJogo(nomeJogo, nomeCliente):
    if type(nomeJogo) != str or type(nomeCliente) != str:
        return 1

    if buscaNoEstoque(nomeJogo):  # checa se o jogo esta disponivel p aluguel
        path = "data/estoqueAluguel.json"
        removeEstoqueAluguel(nomeJogo, 1)
        f = open(path, "r")
        jogos = json.load(f)

        adicionaSaldo(jogos[nomeJogo]['valor'])
        f.close()
        return 0

    compraJogo(nomeJogo, os.environ["CAMINHO_FORNECEDORA_COMPRA"] + str(time.time()) + ".json",
               os.environ["CAMINHO_FORNECEDORA_PREF"] + str(time.time()) + ".json")

    return 3


def devolveJogo(nomeJogo):
    if type(nomeJogo) != str:
        return 2
    if buscaNoEstoque(nomeJogo):
        path = "data/estoqueAluguel.json"
        f = open(path, "r")
        jogos = json.load(f)
        quantAtual = jogos[nomeJogo]['quantidade']
        f.close()

        path = "data/estoqueTotal.json"
        f = open(path, "r")
        jogos = json.load(f)
        quantTotal = jogos[nomeJogo]['quantidade']
        f.close()

        if quantAtual < quantTotal:
            adicionaEstoqueAluguel(nomeJogo, 1)
            return 0

        return 1
    return 3
