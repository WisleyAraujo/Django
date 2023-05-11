from django.contrib.auth.models import User
from django.db import models


# Create your models here 
# cada model, representa uma tabela no banco de dados.
class Category(models.Model):
    name = models.CharField(max_length=65)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug  = models.SlugField() # slug indexado
    prepararion_time = models.IntegerField()
    prepararion_time_unit = models.CharField(max_length=65)
    prepararion_steps = models.TextField()
    prepararion_steps_is_html = models.BooleanField(default=False)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    created_at = models.DateTimeField(auto_now_add=True) #gera uma data no momento da criacao e nao mexe mais nela 
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%d/%m/%Y/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    category
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    def __str__(self):
        return self.title
