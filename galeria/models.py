from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100,)
    foto = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"