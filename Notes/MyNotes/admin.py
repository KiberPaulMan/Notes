from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created']
    list_editable = ['author', ]
    list_filter = ['author', 'created', ]
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}
