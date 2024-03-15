from django.contrib import admin
from .models import Words

class WordsAdmin(admin.ModelAdmin):
    list_display = ('english', 'spanish', 'info', 'box')

# Register your models here.

admin.site.register(Words, WordsAdmin)
