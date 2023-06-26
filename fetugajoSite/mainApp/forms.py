from django import forms

class DevolveJogo(forms.Form):
    your_name = forms.CharField(label="Devolve jogo", max_length=100)

class AlugaJogo(forms.Form):
    nome_user = forms.CharField(label="Nome Jogo", max_length=100)
    aluga_jogo = forms.CharField(label="Aluga jogo", max_length=100)