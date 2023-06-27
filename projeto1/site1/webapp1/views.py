from django.shortcuts import render, redirect

from .models import Livro

from .models import Editora

import random

from .forms import FormUser1

# Create your views here.

def RegistoUser(r):
    msg = ''
    if r.method=='POST':
        form = FormUser1(r.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            msg ='Erro! Dados incorretos!'
    return render(r, 'webapp1/registo.html', {'form':FormUser1(), 'msg':msg})

def livraria(r):
    livros = Livro.objects.order_by('titulo')
    dados = {'dados':livros}
    return render(r,'webapp1/livraria.html',dados)

def editora(r):
    editoras = Editora.objects.order_by('nome')
    dados = {'editora': editoras}
    return render(r, 'webapp1/editora.html', dados)

def cidade(r):
    cidades = ['Lisboa', 'Porto', 'Coimbra', 'Faro', 'Braga', 'Viseu']
    cid = sorted(list(cidades))
    return render(r, 'webapp1/cidades.html', {'cid': cid})

def form1(r):
    print(r.GET)
    try:
        n = int(r.GET['numero'])
    except:
        n = random.randint(1,50)
    return render(r,'webapp1/form1.html', {'dados': range(n)})

def detalhe(r,livro_id):
    livro = Livro.objects.get(pk=livro_id)
    return render(r,'webapp1/detalhe.html', {'liv':livro})

def index(request):
    return render(request,'webapp1/index.html')
    
def pag2(r):
    dados={'nome':'José Domingues','idade': 45}
    return render(r,'webapp1/pagina2.html',dados)