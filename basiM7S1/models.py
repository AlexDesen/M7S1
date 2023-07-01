from django.db import models



class CadastroCliente(models.Model):
    STATUS = (
        ('inadimplente', 'Inadimplente'),
        ('adimplete','Adimplente'),
    )
    nome = models.CharField(verbose_name='Nome',max_length=50)
    idade = models.CharField(verbose_name='Idade', max_length=50)
    telefone = models.CharField(verbose_name='telefone',max_length=50)
    status = models.CharField(verbose_name='Status',max_length=50,choices=STATUS)
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


