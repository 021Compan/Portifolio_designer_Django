from django.db import models
from datetime import datetime
class Fotografia(models.Model):

    nome = models.CharField(max_length=100,)
    foto = models.ImageField(upload_to="fotos/projetos/%Y/%m/%d", blank=True)
    descricao = models.TextField()
    publicada = models.BooleanField(default=False)
    data_Imagem = models.DateTimeField(default=datetime.now , blank = False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
    
class Caricatura(models.Model):

    nome = models.CharField(max_length=100,)
    foto = models.ImageField(upload_to="fotos/caricaturas/%Y/%m/%d", blank=True)
    descricao = models.TextField()
    publicada = models.BooleanField(default=False)
    data_Imagem = models.DateTimeField(default=datetime.now , blank = False)

    def __str__(self):
        return f'Caricatura [nome={self.nome}]'