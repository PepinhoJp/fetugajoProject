import json
from saldo import removeSaldo, verificaSaldo
from estoque import AdicionaEstoqueTotal

def adicionaPreferencia(nomejogo, path):
    data={"tipo":"preferencia-novo-jogo", "dados": {"nome": nomejogo, "preco": 5, "fabricante": "Microny"}}
    path = path + nomejogo
    with open(path , "w") as arq:
        json.dump(data,arq,indent=4) 


def compraJogo(nomejogo, pathval, pathpref):
    preco= recebePrecoCompra(nomejogo, pathval)
    if type(preco)== str:
        adicionaPreferencia(nomejogo, pathpref)
        return
    if verificaSaldo()>=preco:
        removeSaldo(preco)
        AdicionaEstoqueTotal(nomejogo)
    else:
        adicionaPreferencia(nomejogo, pathpref)
    return

def recebePrecoCompra(nomejogo, path):
    with open(path, 'r') as arq:
        dados_json = json.load(arq)
        for el in range(len(dados_json)):
            if nomejogo== dados_json[el]["nome"]: ##jogo existe e está nessa linha 
                preco = dados_json[el]["preco"]
                return preco
        ##nao existe o nomejogo no arquivo
    return "jogo não consta na tabela de preços"
