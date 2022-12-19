from django.shortcuts import render, get_object_or_404
from .models import Receita


def index(requisicao):

    receitas = Receita.objects.all()

    dados ={
        'receitas' : receitas
    }
    return render(requisicao, 'index.html', dados)

def receita(requisicao, receita_id):
    receita = get_object_or_404(Receita, pk = receita_id)
    receita_a_exeibir = {
        'receita' : receita 
    }
    return render(requisicao, 'receita.html', receita_a_exeibir)