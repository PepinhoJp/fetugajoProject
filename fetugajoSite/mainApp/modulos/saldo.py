import json

def verificaSaldo():
    f = open("data/saldo.json", "r")
    saldoEmpresa = json.load(f)

    return saldoEmpresa['SaldoEmpresa']

def adicionaSaldo( valor):
    if type(valor) != int:
        return 1
    with open("data/saldo.json") as f:
        saldoEmpresa = json.load(f)

        atual = saldoEmpresa['SaldoEmpresa']
        saldoEmpresa['SaldoEmpresa'] = float(atual) + valor
        json.dump(saldoEmpresa, open("data/saldo.json", "w"), indent=4)
    return 0

def removeSaldo( valor):
    if type(valor) != int:
        return 1
    with open("data/saldo.json") as f:
        saldoEmpresa = json.load(f)

        atual = saldoEmpresa['SaldoEmpresa']
        saldoEmpresa['SaldoEmpresa'] = float(atual) - valor
        json.dump(saldoEmpresa, open("data/saldo.json", "w"), indent=4)
    return 0