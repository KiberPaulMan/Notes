# Generated by Django 4.1 on 2022-08-17 13:38

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyNotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=255), unique=True),
        ),
    ]