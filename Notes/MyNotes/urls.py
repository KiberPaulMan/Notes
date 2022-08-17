from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notes, name='all_notes'),
    path('create/', views.create_note, name='create_note'),
    path('update/<slug:slug>', views.update_note, name='update_note'),
    path('<slug:note_slug>/', views.get_note, name='get_note'),
]