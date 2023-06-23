import json
def verificaCliente(path, nome):
    
    f = open(path, "r")
    c = json.load(f)
    f.close()
    if nome in c:
        return True
    return False

def criaCliente(path, nomeCliente):
    with open(path) as f:
        f = open(path, "r")
        jogos = json.load(f)
        jogos[nomeCliente] = {}
        json.dump(jogos, open(path, "w"), indent=4)
    return

def removeCliente(path, nome):
    f = open(path, "r")
    c = json.load(f)
    
    if verificaCliente(path, nome):
        del c[nome]
                
