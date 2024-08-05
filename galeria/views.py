from django.shortcuts import render
from galeria.models import Fotografia

def home(request):
    return render(request, 'front-end/home.html')

def portfolio(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'front-end/projetos.html', {'cards': fotografias})

def caricaturas(request):
    return render(request, 'front-end/caricaturas.html')

def sobre(request):
    return render(request, 'front-end/sobre.html')