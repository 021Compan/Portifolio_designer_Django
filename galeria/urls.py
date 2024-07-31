from django.urls import path
from galeria.views import home, portfolio, caricaturas, sobre

urlpatterns = [
        path('', home, name='home'),
        path('projetos/',portfolio, name='projetos'),
        path('caricaturas/',caricaturas, name='caricaturas'),
        path('sobre/',sobre, name='sobre')
]