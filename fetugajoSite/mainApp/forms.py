from django import forms

class DevolveJogo(forms.Form):
    your_name = forms.CharField(label="Devolve jogo", max_length=100)