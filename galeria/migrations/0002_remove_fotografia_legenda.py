# Generated by Django 5.0.7 on 2024-08-06 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='legenda',
        ),
    ]
