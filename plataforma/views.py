from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def pacientes (request):
    return render(request, 'paciente.html')