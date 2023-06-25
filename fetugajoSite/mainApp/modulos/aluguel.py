import json
from estoque import *
from cliente import *
from saldo import *


def validaAluguel(f):
    def valida(nomeJogo, nomeCliente):
        if verificaCliente(nomeCliente):
            return f(nomeJogo, nomeCliente)
        return 2

    return valida


@validaAluguel
def alugaJogo(nomeJogo, nomeCliente):
    if buscaNoEstoque(nomeJogo):  # checa se o jogo esta disponivel p aluguel
        path = "data/estoqueAluguel.json"
        removeEstoqueAluguel(nomeJogo, 1)
        f = open(path, "r")
        jogos = json.load(f)

        adicionaSaldo(jogos[nomeJogo]['valor'])
        f.close()
        return 0

    compraJogo(nomeJogo)

    return 1

def devolveJogo(nomeJogo):
    adicionaEstoqueAluguel(nomeJogo, 1)
    return
