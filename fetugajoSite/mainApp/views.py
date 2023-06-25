from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .modulos.estoque import *
from .forms import *

import os
from .modulos.saldo import verificaSaldo

def index(request):
    context = {}
    context['saldo'] = verificaSaldo()
    context['estoque'] = verificaEstoque()

    if request.method == "POST":
        nomeJogo = request.POST.get('nome_jogo')
        print(nomeJogo)
    else:
        form = DevolveJogo()

    context['form'] = form

    return render(request, 'principal.html', context=context)