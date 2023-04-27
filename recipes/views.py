from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'WisleyAraujo',
    })


def contato(request):
    return render(request, 'recipes/contato.html', {
        'fone': '996241946' 
    })


def sobre(request):
    return HttpResponse('Sobre1')
