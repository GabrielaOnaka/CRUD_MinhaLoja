from django.shortcuts import render,redirect
import requests
from .models import Pessoa
from django.contrib import messages
from .forms import PessoaForm

def raiz(request):
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao = cotacao.json()
    cotacao_dolar = cotacao['USDBRL']['bid']
    cotacao_dolar2 = cotacao_dolar + " ; " + cotacao['USDBRL']['create_date']
    print(cotacao_dolar)
    print(cotacao_dolar2)
    return render(request, 'home.html', {'cotacao_dolar': cotacao_dolar, 'data': cotacao_dolar2})


def clientes(request):
    nome = request.POST.get("nome")
    cpf = request.POST.get("cpf")
    email = request.POST.get("email")
    endereco = request.POST.get("endereco")
    cidade = request.POST.get("cidade")
    uf = request.POST.get("uf")

    if nome == '' or cpf == '' or email == '' or endereco == '' or cidade == '':
        messages.info(request, 'Preencha os campos abaixo por favor!')
        return redirect('/loja/home/')
    else:
        if Pessoa.objects.filter(cpf=cpf).exists():
            messages.info(request, 'CPF já cadastrado! Por favor tente novamente... ')
            return redirect('/loja/clientes/')
        else:
            pessoas = Pessoa(
                nome=nome,
                cpf=cpf,
                email=email,
                endereco=endereco,
                cidade=cidade,
                uf=uf,
            )
            pessoas.save()
        return cadastro_consultar(request)

def home(request):
    return render(request,'clientes.html')

def produto(request):
    return render(request, 'produto.html')


def cadastro(request):
    cadastro_todos = Pessoa.objects.all()
    return render(request, 'cadastro.html', {'cadastro_todos': cadastro_todos})


def cadastro_consultar(request):
    cadastro_ultimo = Pessoa.objects.last()
    return render(request, 'clientes.html', {'cadastro_ultimo': cadastro_ultimo})


def editar(request, id):
    clientes = Pessoa.objects.filter(id=id).first()
    form = PessoaForm(instance=clientes)

    if (request.method == 'POST'):
        form = PessoaForm(request.POST, instance=clientes)
        if form.is_valid():
            clientes.save()
            return redirect('/loja/cadastro/')
        else:
            return render(request, 'editar.html', {'form': form, 'clientes': clientes})
    else:
        return render(request, 'editar.html', {'form': form, 'clientes': clientes})

def remover(request, id):
    delete_cliente = Pessoa.objects.get(id=id)
    delete_cliente.delete()
    return cadastro(request)
