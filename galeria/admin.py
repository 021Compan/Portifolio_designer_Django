from django.contrib import admin

from galeria.models import Fotografia, Caricatura

class listandoFotos(admin.ModelAdmin):
    list_display = ("id", "nome", "foto")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")

class listandoCaricaturas(admin.ModelAdmin):
    list_display = ("id", "nome", "foto")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")

admin.site.register(Fotografia, listandoFotos,)
admin.site.register(Caricatura, listandoCaricaturas)


