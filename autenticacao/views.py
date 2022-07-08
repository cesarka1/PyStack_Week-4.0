from django.shortcuts import redirect, render
from django.http import HttpResponse
from .utils import password_is_valid
from django.shortcuts import redirect

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')
        
        return HttpResponse(f'Usuario: {usuario} \n Email: {email} Senha: {senha} Confimar Senha {confirmar_senha}')

def logar(request):
    return HttpResponse("Você está na página de Login")

