import json
def buscaNoEstoque(nomeJogo):
    path = "data/estoqueAluguel.json"
    if type(nomeJogo) != str:
        return 2
    f = open(path, "r")
    jogos = json.load(f)

    if nomeJogo in jogos:
        if (jogos[nomeJogo]['quantidade'] > 0):
            f.close()
            return True
    f.close()
    return False

def adicionaEstoqueAluguel(nomeJogo, qnt):
    if type(nomeJogo) != str:
        return 1
    if type(qnt) != int:
        return 2
    path = "data/estoqueAluguel.json"
    with open(path, "r") as f:
        jogos = json.load(f)
        # Se o jogo ja esta no estoque
        if nomeJogo in jogos:
            atual = jogos[nomeJogo]['quantidade']
            jogos[nomeJogo]['quantidade'] = atual + qnt
        else:
            #Se o jogo nao esta no estoque, adiciona ele
            jogos[nomeJogo] = {"quantidade": qnt, "valor": 10}
        json.dump(jogos, open(path, "w"), indent=4)
    return 0

def adicionaEstoqueTotal(nomeJogo, qnt):
    if type(nomeJogo) != str:
        return 1
    if type(qnt) != int:
        return 2
    path = "data/estoqueTotal.json"
    with open(path, "r") as f:
        jogos = json.load(f)
        # Se o jogo ja esta no estoque
        if nomeJogo in jogos:
            atual = jogos[nomeJogo]['quantidade']
            jogos[nomeJogo]['quantidade'] = atual + qnt
        else:
            #Se o jogo nao esta no estoque, adiciona ele
            jogos[nomeJogo] = {"quantidade": qnt, "valor": 10}
        json.dump(jogos, open(path, "w"), indent=4)
    return 0

def removeEstoqueAluguel(nomeJogo, qnt):
    if type(nomeJogo) != str:
        return 4
    if type(qnt) != int:
        return 3
    path = "data/estoqueAluguel.json"
    with open(path, "r") as f:
        jogos = json.load(f)
        # Se o jogo ja esta no estoque
        if nomeJogo in jogos:

            atual = jogos[nomeJogo]['quantidade']
            if (atual - qnt < 0):
                return 2
            if (atual - qnt == 0):
                jogos.pop(nomeJogo)
            else:
                jogos[nomeJogo]['quantidade'] = atual - qnt
        else:
            return 1

        json.dump(jogos, open(path, "w"), indent=4)
    return 0

def verificaEstoque():
    pathAluguel = "data/estoqueAluguel.json"
    pathTotal = "data/estoqueTotal.json"

    fAluguel = open(pathAluguel, "r")
    fTotal = open(pathTotal, "r")
    jogosAlugados = json.load(fAluguel)
    jogosTotal = json.load(fTotal)

    dicRetorno = {}

    for jogo in jogosTotal:
        dicAuxiliar = {}

        #Qnt total
        dicAuxiliar['total'] = jogosTotal[jogo]['quantidade']

        #Alugados
        dicAuxiliar['alugados'] = jogosTotal[jogo]['quantidade'] - jogosAlugados[jogo]['quantidade']

        #Disponiveis para aluguel
        dicAuxiliar['disponiveis'] = jogosAlugados[jogo]['quantidade']

        dicRetorno[jogo] = dicAuxiliar

    fTotal.close()
    fAluguel.close()

    return dicRetorno
