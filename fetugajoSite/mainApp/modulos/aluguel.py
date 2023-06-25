import json
import cliente.py
import estoque.py
import compra.py

def validaAluguel(f):
    def valida(nomeJogo, nomeCliente):
        if verificaCliente(nomeCliente):
            return alugaJogo(nomeJogo, nomeCliente)
        return 2
    return valida

@validaAluguel
def alugaJogo(nomeJogo, nomeCliente):
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

def devolveJogo(nomeJogo):
    path = "data/estoqueAluguel.json"
    with open(path, "r") as f:
        jogos = json.load(f)
        atual = jogos[nomeJogo]['quantidade']
        jogos[nomeJogo]['quantidade'] = atual + qnt
    return
  
