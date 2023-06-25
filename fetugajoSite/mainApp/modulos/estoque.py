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

def adicionaEstoqueAluguel(nomeJogo, qnt):
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
    return

def adicionaEstoqueTotal(nomeJogo, qnt):
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
    return

def removeEstoqueAluguel(nomeJogo, qnt):
    path = "data/estoqueAluguel.json"
    with open(path, "r") as f:
        jogos = json.load(f)
        # Se o jogo ja esta no estoque
        if nomeJogo in jogos:

            atual = jogos[nomeJogo]['quantidade']
            if (atual - qnt < 0):
                return "Nao ha suficiente desse jogo para remover"
            if (atual - qnt == 0):
                jogos.pop(nomeJogo)
            else:
                jogos[nomeJogo]['quantidade'] = atual - qnt
        else:
            return "Jogo nao esta no estoque para fazer a remoção"

        json.dump(jogos, open(path, "w"), indent=4)
    return

def removeEstoqueAluguel(nomeJogo, qnt):
    path = "data/estoqueAluguel.json"
    with open(path, "r") as f:
        jogos = json.load(f)
        # Se o jogo ja esta no estoque
        if nomeJogo in jogos:

            atual = jogos[nomeJogo]['quantidade']
            if (atual - qnt < 0):
                return "Nao ha suficiente desse jogo para remover"
            if (atual - qnt == 0):
                jogos.pop(nomeJogo)
            else:
                jogos[nomeJogo]['quantidade'] = atual - qnt
        else:
            return "Jogo nao esta no estoque para fazer a remoção"

        json.dump(jogos, open(path, "w"), indent=4)
    return

def exibeEstoque():
    pathAluguel = "data/estoqueAluguel.json"
    pathTotal = "data/estoqueTotal.json"

    fAluguel = open(pathAluguel, "r")
    fTotal = open(pathTotal, "r")
    jogosAlugados = json.load(fAluguel)
    jogosTotal = json.load(fTotal)

    for jogo in jogosTotal:
        print(jogo + ":")
        print("\tPreço: " + str(jogosTotal[jogo]['valor']))
        print("\tQuantidade total: " + str(jogosTotal[jogo]['quantidade']))
        print("\tAlugados: " + str(jogosTotal[jogo]['quantidade'] - jogosAlugados[jogo]['quantidade']))
        print("\tDisponiveis para aluguel: " + str(jogosAlugados[jogo]['quantidade']))

    fTotal.close()
    fAluguel.close()

    return
