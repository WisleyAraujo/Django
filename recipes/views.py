from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'WisleyAraujo',
    })


def contato(request):
    return HttpResponse('Contact1')


def sobre(request):
    return HttpResponse('Sobre1')
