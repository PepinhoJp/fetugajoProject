import json
def buscaNoEstoque(path, nomeJogo):
    f = open(path, "r")
    jogos = json.load(f)

    if nomeJogo in jogos:
        if (jogos[nomeJogo]['quantidade'] > 0):
            f.close()
            return True
    f.close()
    return False

def adicionaEstoqueAluguel(path, nomeJogo, qnt):
    with open(path) as f:
        f = open(path, "r")
        jogos = json.load(f)
        # Se o jogo ja esta no estoque
        if nomeJogo in jogos:
            atual = jogos[nomeJogo]['quantidade']
            jogos[nomeJogo]['quantidade'] = atual + qnt
        else:
            #Se o jogo nao esta no estoque, adiciona ele
            jogos[nomeJogo] = {"quantidade": qnt, "valor": 10}
        json.dump(jogos, open(path, "w"), indent=4)
    return