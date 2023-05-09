from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe #importando a function


# 
def home(resquest):
    return render(resquest, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(4)]
    })
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datail_page': True
    })
