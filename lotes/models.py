from django.db import models
import datetime
import io
import time
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User
# Create your models here.
# Padrões e boas práticas para nome de models no Django:
# CamelCase (PascalCase)

class StatusProprietario(models.TextChoices):
    PETROBRAS = 'Petrobras', 'Petrobras'
    CONSORCIO = 'Consorcio', 'Consorcio'
    
class Lote(models.Model):
# Padrões para nomear choices no Django
# Use letras MAIÚSCULAS para o nome da constante
# Isso segue o padrão Python para constantes.
# Exemplo: STATUS_CHOICES, TIPO_USUARIO, CATEGORIA_PRODUTO

    PRIORIDADE_CHOICES = (
        ('Urgente', 'Urgente'),
        ('Alta', 'Alta'),
        ('Média', 'Média'),
        ('Baixa', 'Baixa')
    )
    STATUS_CHOICES = (
        
        ('Pendente data de Recebimento', 'Pendente data de Recebimento'),
        ('Pendente de Pagamento', 'Pendente de Pagamento'),
        ('Pendente de Entrega', 'Pendente de Entrega'),
        ('Pendente de Medição', 'Pendente de Medição'),
        ('Pendente de Conciliação', 'Pendente de Conciliação'),
        ('Cancelado Pendente de Conciliação', 'Cancelado Pendente de Conciliação'),
        ('Conciliado', 'Conciliado'),
        ('Cancelado Conciliado', 'Cancelado Conciliado'),
        ('Em Negociação-Superbid', 'Em Negociação-Superbid'),
        ('Sucateado Pendente de Baixa', 'Sucateado Pendente de Baixa'),
        ('Sucateado Baixado', 'Sucateado Baixado'),
        ('Em Leilão', 'Em Leilão'),
        ('Entrega Programada', 'Entrega Programada'),
        ('Nota Pendente de Assinatura', 'Nota Pendente de Asssinatura'),

        ('', '')
    )
    TIPOVENDA_CHOICES = (
        ('Desinvestimento','Desinvestimento'),
        ('Sucateamento','Sucateamento'),
        ('Vendido', 'Vendido'),
        
      
        ('Leilão', 'Leilão'),
        ('', '')
    )
    MATERIAL_CHOICES = (
        ('Inservivel','Inservivel'),
        ('Residuo Valorizavel', 'Residuo Valorizavel')
      
    )
    
    ANO_INICIO = 2020
    ANO_CHOICES = [(ano, ano) for ano in range(ANO_INICIO, date.today().year + 1)]
    
    WRITEDOWN_CHOICES = (
        ('', ''),
        ('WRITE DOWN COMPLETO', 'WRITE DOWN COMPLETO'),
        ('WRITE DOWN PARCIAL','WRITE DOWN PARCIAL')

    )

    ENTREGA_CHOICES = (
        ('SEM ENTREGA', 'SEM ENTREGA'),
        ('ENTREGA PARCIAL', 'ENTREGA PARCIAL'),
        ('ENTREGA FINALIZADA','ENTREGA FINALIZADA')

    )
    
    MOTIVO_CHOICES = (
        ('MANIPULADORA QUEBRADA', 'MANIPULADORA QUEBRADA'),
        ('CLIENTE DESISTIU', 'CLIENTE DESISTIU'),
        ('REPROGRAMADO PELO CLIENTE','REPROGRAMADO PELO CLIENTE')

    )

    Codigo = models.CharField(primary_key=True, max_length=50, null=False)
    # Gerencia = models.ForeignKey(GERENCIA, on_delete=models.SET_NULL, null=True)
    # Proprietario = models.CharField(choices=StatusProprietario max_length=50, null=False)
    # Leilao = models.ForeignKey(LEILAO, on_delete=models.SET_NULL, null=True, blank=True)
    Al = models.CharField(max_length=50, null=False)
    Ano = models.IntegerField(choices=ANO_CHOICES)
    Responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
 
    
    LocalArmazenamento = models.CharField(max_length=50, null=True, blank=True)
    IsaSipa = models.CharField(max_length=50, null=True, blank=True)
    DataSipa = models.DateField(null=True, blank=True)
    TipoVenda = models.CharField(choices=TIPOVENDA_CHOICES, max_length=50, null=True, blank=True)
    TipoMaterial = models.CharField(choices=MATERIAL_CHOICES, max_length=50, null=True, blank=True)
   
    IsaEnvioArm = models.CharField(max_length=50, null=True, blank=True)
    DataEnvoArm = models.DateField(null=True, blank=True)
    DataRecebimentoLote = models.DateField(null=True, blank=True)
    PrazoEntrega = models.DateField(null=True, blank=True)
    DataEntrega = models.DateField(null=True, blank=True)
    PrazoConciliação = models.DateField(null=True, blank=True)
    DataConciliação =models.DateField(null=True, blank=True)
    DataUltimaBaixa=models.DateField(null=True, blank=True)
    PrazodeBaixa=models.DateField(null=True, blank=True)
    DataPagamento=models.DateField(null=True, blank=True)
    PrazoPagamento = models.DateField(null=True, blank=True)
    DataCancelamento=models.DateField(null=True, blank=True)
    Cancelado = models.BooleanField(default=False)
    Prioridade =models.CharField(max_length=50, choices=PRIORIDADE_CHOICES, null=True, blank=True)
    Status =models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    DataMedicao =models.DateField(null=True, blank=True)
    PrazoMedicao =models.DateField(null=True, blank=True)
    PrazoConciliacaoCancelado=models.DateField(null=True, blank=True)
    DataConciliacaoCancelado=models.DateField(null=True, blank=True)
    DataAuditoria=models.DateField(null=True, blank=True)
    DataNegociacao=models.DateField(null=True, blank=True)
    EmNegociacao=models.BooleanField(default=False)
    DataPagamentoLoteEx=models.DateField(null=True, blank=True)
    WriteDownStatus =models.CharField(max_length=50, choices=WRITEDOWN_CHOICES, null=True, blank=True)
    DtatusDeEntrega =models.CharField(max_length=50, choices=ENTREGA_CHOICES, null=True, blank=True,default='SEM ENTREGA')
    PrazoEntregaAdicional = models.IntegerField(default=0)
    PrazoPagamentoAdicional = models.IntegerField(default=0)
    DataCadastroUltimaNota = models.DateField(null=True, blank=True)
    DataSolicitacaoConciliacao = models.DateField(null=True, blank=True)
    DataSolicitacaoConciliacaoCancelado = models.DateField(null=True, blank=True)
    Perdeuprazoentrega =models.BooleanField(default=False)
    MotivoPercaPrazo = models.CharField(max_length=100, null=True, blank=True)
    
    Notificacao = models.BooleanField(default=False)
  
    def __str__(self):
        return f"{self.Codigo}/{self.Tipo}"   
  
   
    
   