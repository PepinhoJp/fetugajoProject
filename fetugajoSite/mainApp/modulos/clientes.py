import json

def verificaCliente(path, nome):
    
    f = open(path, "r")
    c = json.load(f)
    f.close()
    if nome in c:
        return True
    return False
