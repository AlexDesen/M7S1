from django.urls import path,include
from basiM7S1.views import Cliente,CadastrandoCliente

app_name = 'cliente'

urlpatterns = [
    path('cadastro/', Cliente, name='cliente'),
      path('cadastrando/', CadastrandoCliente, name='cadastrando'),
]
