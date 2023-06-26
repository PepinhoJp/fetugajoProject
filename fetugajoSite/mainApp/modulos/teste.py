from saldo import *
from aluguel import *
from compra import *
from estoque import *
from cliente import *

def teste(ret, retornoEsperado):
    if ret == retornoEsperado:
        print("TesteOK")
    else:
        print("Retorno diferente do esperado")
    return


teste(criaCliente("João Pedro Magalhães"), 0)
teste(criaCliente(1),1)
teste(criaCliente("João Pedro Magalhães"), 2)
teste(removeCliente("João Pedro Magalhães"),0)
teste(removeCliente("Felipe Barcellos"),1)
teste(verificaCliente("Matheus origami"),1)
teste(verificaCliente("Felipe Barcellos"),0)
teste(removeEstoqueAluguel("Monopoly",1),0)
teste(removeEstoqueAluguel("dobble",1),1)
teste(removeEstoqueAluguel("War",1),2)
teste(removeEstoqueAluguel("Monopoly","abc"),3)
teste(removeEstoqueAluguel(1,1),4)
teste(adicionaEstoqueAluguel("Monopoly",1),0)
teste(adicionaEstoqueAluguel(1,1),1)
teste(adicionaEstoqueAluguel("Monopoly","abc"),2)
teste(adicionaEstoqueTotal("Taco,gato,pizza",1),0)
teste(adicionaEstoqueTotal(1,1),1)
teste(adicionaEstoqueTotal("Taco,gato,pizza","abc"),2)
teste(buscaNoEstoque("Monopoly"),0)
teste(buscaNoEstoque("coup"),1)
teste(buscaNoEstoque(1),2)
teste(alugaJogo("Monopoly", "João Pedro Magalhães"),0)
teste(alugaJogo(2, "João Pedro Magalhães"),1)
teste(alugaJogo("Monopoly", "Carolina Lira"), 2)
teste(alugaJogo("Cards Against Humanity", "João Pedro Magalhães"),3)
teste(devolveJogo("Monopoly"),0)
teste(devolveJogo("Detetive"),1)
teste(devolveJogo(3),2)
teste(adicionaSaldo(1),0)
teste(adicionaSaldo(-1),1)
teste(removeSaldo("1"),0)
teste(removeSaldo(-1),1)
##teste(compraJogo(!, "data/tabela_de_valores.json", "data/"),0)
##teste(compraJogo("dobble3", "data/tabela_de_valores.json", "data/"),-1)
teste(adicionaPreferencia("Monopoly", "data/"),0)
teste(adicionaPreferencia(5, "data/"),1)
teste(recebePrecoCompra("Monopoly", "data/"),0)
teste(recebePrecoCompra(1, "data/"),0)
teste(recebePrecoCompra("Quest", "data/"),-1)
