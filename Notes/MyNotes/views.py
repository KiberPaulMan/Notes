from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Note
from .forms import NoteForm


def get_notes(request):
    notes = Note.objects.all()
    return render(request, 'MyNotes/notes.html', {'notes': notes})


def get_note(request, note_slug):
    note = get_object_or_404(Note, slug=note_slug)
    return render(request, 'MyNotes/note.html', {'note': note})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        # form.save(commit=False)
        # t1 = form.cleaned_data['title']
        # print('TITLE = ', t1)
        if form.is_valid():
            form.save()
            return redirect('all_notes')
    else:
        form = NoteForm()
    return render(request, 'MyNotes/create.html', {'form': form})


def update_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    form = NoteForm(note)
    # form.title = note.title
    # form.description = note.description
    # form.author = note.author
    # print(form.title, form.description, form.author)
    # form.save(commit=False)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('get_note', slug)
    return render(request, 'MyNotes/update.html', {'form': form})


def delete_note(request, slug):
    if slug:
        try:
            note = get_object_or_404(Note, slug=slug)
        except:
            print('Что-то пошло не так!')
        note.delete()
    return redirect('all_notes')
