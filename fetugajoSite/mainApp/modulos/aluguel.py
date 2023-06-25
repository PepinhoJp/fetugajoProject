import json
import cliente.py
import estoque.py
import compra.py

def alugaJogo(nomeJogo, nomeCliente):
    if verificaCliente(nomeCliente):
        if buscaNoEstoque(nomeJogo): #checa se o jogo esta disponivel p aluguel
            path = "data/estoqueAluguel.json"
            removeEstoqueAluguel(nomeJogo, 1)
            f = open(path, "r")
            jogos = json.load(f)

            adicionaSaldo(jogos[nomeJogo]['valor'])
            f.close() 
            return 0
            
        compraJogo(nomeJogo)
            
        return 1
    return 2

def devolveJogo(nomeJogo):
    adicionaEstoqueAluguel(nomeJogo)
    return
