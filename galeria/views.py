from django.shortcuts import render


def home(request):
    return render(request, 'front-end/home.html')

def portfolio(request):
    return render(request, 'front-end/projetos.html')

def caricaturas(request):
    return render(request, 'front-end/caricaturas.html')

def sobre(request):
    return render(request, 'front-end/sobre.html')