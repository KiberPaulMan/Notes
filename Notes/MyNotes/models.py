from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created', '-updated']

    def __str__(self):
        return self.title[:50]