import json

def verificaSaldo(path):
    f = open(path, "r")
    saldoEmpresa = json.load(f)

    return saldoEmpresa['SaldoEmpresa']

def adicionaSaldo(path, valor):
    with open(path) as f:
        saldoEmpresa = json.load(f)

        atual = saldoEmpresa['SaldoEmpresa']
        saldoEmpresa['SaldoEmpresa'] = float(atual) + valor
        json.dump(saldoEmpresa, open(path, "w"), indent=4)

def removeSaldo(path, valor):
    with open(path) as f:
        saldoEmpresa = json.load(f)

        atual = saldoEmpresa['SaldoEmpresa']
        saldoEmpresa['SaldoEmpresa'] = float(atual) - valor
        json.dump(saldoEmpresa, open(path, "w"), indent=4)