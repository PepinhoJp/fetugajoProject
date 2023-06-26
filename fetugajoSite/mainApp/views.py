from django.shortcuts import render

# Create your views here.
from .modulos.aluguel import *
from django.views.decorators.csrf import csrf_protect
from .modulos.saldo import verificaSaldo
from .modulos.cliente import *

@csrf_protect
def index(request):
    context = {}
    context['saldo'] = verificaSaldo()
    context['estoque'] = verificaEstoque()
    context['clientes'] = exibeClientes()

    if request.method == "POST":
        if ('jogo' in request.POST):
            nomeJogo = request.POST.get('jogo')
            devolveJogo(nomeJogo)
        elif('jogoAluga' in request.POST):
            nomeJogo = request.POST.get('jogoAluga')
            nomeCliente = request.POST.get('cliente')
            alugaJogo(nomeJogo, nomeCliente)
        elif ('cadastraCliente' in request.POST):
            nomeCliente = request.POST.get('cadastraCliente')
            criaCliente(nomeCliente)
        elif ('removeCliente' in request.POST):
            nomeCliente = request.POST.get('removeCliente')
            removeCliente(nomeCliente)

    return render(request, 'principal.html', context=context)