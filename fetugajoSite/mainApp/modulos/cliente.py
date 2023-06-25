import json
def verificaCliente(nomeCliente):
    path = "data/clientes.json"
    f = open(path, "r")
    c = json.load(f)
    f.close()
    if nomeCliente in c:
        return True
    return False

def criaCliente(nomeCliente):
    path = "data/clientes.json"
    with open(path) as f:
        f = open(path, "r")
        jogos = json.load(f)
        jogos[nomeCliente] = {}
        json.dump(jogos, open(path, "w"), indent=4)
    return

def removeCliente(nomeCliente):
    path = "data/clientes.json"
    f = open(path, "r")
    c = json.load(f)
    
    if verificaCliente(path, nomeCliente):
        c.pop(nomeCliente)

def exibeClientes():
    path = "data/clientes.json"
    f = open(path, "r")
    c = json.load(f)
    f.close()
    return c
