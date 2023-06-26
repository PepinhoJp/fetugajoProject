import json
from .estoque import *
from .cliente import *
from .saldo import *
from .compra import *

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

    compraJogo(nomeJogo, "", "")

    return 1

def devolveJogo(nomeJogo):
    if type(nomeJogo) != str:
        return 2
    
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
