from django.contrib import admin
from.models import Category,Tag,Post,Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','category','create_at']
    search_fields = ['title','content']
