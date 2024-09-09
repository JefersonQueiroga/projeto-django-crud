from django.shortcuts import render,redirect


# Create your views here.
def index(request):
        return render(request,'escola/index.html')


def cadastrar(request):
   return render(request,'escola/cadastro_aluno.html')

 

