from django.contrib import admin

from .models import Blog, Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...
class RecipeAdmin(admin.ModelAdmin):
    ...
class BlogAdmin(admin.ModelAdmin):
    ...

admin.site.register(Blog, BlogAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category,CategoryAdmin)
