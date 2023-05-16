from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe  # importando a function

from .models import Recipe


# 
def home(resquest):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(resquest, 'recipes/pages/home.html', context={
        'recipes': recipes
    })
def category(resquest, category_id):
    recipes = Recipe.objects.filter(
        category__id = category_id
        ).order_by('-id')
    return render(resquest, 'recipes/pages/home.html', context={
        'recipes': recipes
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datail_page': True
    })
