from django.contrib import admin
from .models import Category, Word, GameSession

# Register your models here.
admin.site.register(Category)
admin.site.register(Word)
admin.site.register(GameSession)