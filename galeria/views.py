from django.shortcuts import render
from galeria.models import Fotografia, Caricatura

def home(request):
    return render(request, 'front-end/home.html')

def portfolio(request):
    fotografias = Fotografia.objects.order_by("data_Imagem").filter(publicada = True)
    return render(request, 'front-end/projetos.html', {'cards': fotografias})

def caricaturas(request):
    caricatura = Caricatura.objects.order_by("data_Imagem").filter(publicada =  True)
    return render(request, 'front-end/caricaturas.html', {'cards': caricatura})

def sobre(request):
    return render(request, 'front-end/sobre.html')