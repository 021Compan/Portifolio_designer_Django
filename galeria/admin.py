from django.contrib import admin

from galeria.models import Fotografia, Caricatura

class listandoFotos(admin.ModelAdmin):
    list_display = ("id", "nome", "foto", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")
    list_editable = ("publicada",)
    list_per_page = 10

class listandoCaricaturas(admin.ModelAdmin):
    list_display = ("id", "nome", "foto", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")
    list_per_page = 10

admin.site.register(Fotografia, listandoFotos,)
admin.site.register(Caricatura, listandoCaricaturas)


