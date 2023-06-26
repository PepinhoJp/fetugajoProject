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
    if type(nomeCliente) != str:
        return 1
    if verificaCliente(nomeCliente):
        return 2
    path = "data/clientes.json"
    with open(path) as f:
        jogos = json.load(f)
        jogos[nomeCliente] = {}
        json.dump(jogos, open(path, "w"), indent=4)
    return 0

def removeCliente(nomeCliente):
    path = "clientes.json"
    with open(path, "r") as f:
       clientes = json.load(f)
       if verificaCliente(nomeCliente):
           clientes.pop(nomeCliente)
           f.close()
           json.dump(clientes, open(path, "w"), indent=4)
           return 0
       return 1

def exibeClientes():
    path = "data/clientes.json"
    f = open(path, "r")
    c = json.load(f)
    f.close()
    return c
