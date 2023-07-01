from django.contrib import admin
from basiM7S1.models import CadastroCliente

@admin.register(CadastroCliente)
class CadastroClienteAdimin(admin.ModelAdmin):
    list_display = ['nome','idade','telefone']