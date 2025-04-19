from django.http import HttpResponse
from django.shortcuts import render

#View functions
def home(request):
    return HttpResponse('Página inicial')

def contato(request):
    return HttpResponse('Meus contatos')

def sobre(request):
    return HttpResponse('Sobre meu negócio')

