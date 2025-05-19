from django import forms
from lotes.models import Lote
import datetime
from django.contrib.auth.models import User
import time
from datetime import date, datetime, timedelta

class FormConsultarLote(forms.Form):
    lote = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'data-role':'tagsinput'}),label="Lote:", required=False)
    
    PRIORIDADE_CHOICES = (
        ('Urgente', 'Urgente'),
        ('Alta', 'Alta'),
        ('Média', 'Média'),
        ('Baixa', 'Baixa')
    )
    STATUS_CHOICES =(  
        ('Pendente data de Recebimento', 'Pendente data de Recebimento'),
        ('Pendente de Pagamento', 'Pendente de Pagamento'),
        ('Pendente de Entrega', 'Pendente de Entrega'),
        ('Pendente de Medição', 'Pendente de Medição'),
        ('Pendente de Conciliação', 'Pendente de Conciliação'),
        ('Conciliado', 'Conciliado'),
        ('Cancelado Pendente de Conciliação', 'Cancelado Pendente de Conciliação'),
        ('Cancelado Conciliado', 'Cancelado Conciliado'),
        ('Sucateado Pendente de Baixa', 'Sucateado Pendente de Baixa'),
        ('Sucateado Baixado', 'Sucateado Baixado'),
        ('Em Negociação-Superbid', 'Em Negociação-Superbid'),
        ('Em Leilão', 'Em Leilão'),
        ('Entrega Programada', 'Entrega Programada'),
        ('Nota Pendente de Assinatura', 'Nota Pendente de Asssinatura'),
        ('', '')
        )
    
    VENDA_CHOICES = (('Desinvestimento','Desinvestimento'),('Sucateamento','Sucateamento'), ('Vendido', 'Vendido'),('Sucata Vendido', 'Sucata Vendido'),('Leilão', 'Leilão'),('', ''))
    ARMAZEM_CHOICES = (('Macaé - RJ', 'Macaé - RJ'), ('Rio de Janeiro - RJ', 'Rio de Janeiro - RJ'),('TLI - RJ', 'TLI - RJ'), ('Cubatão - SP','Cubatão - SP'))
    PROPRIETARIO_CHOICES = (('Petrobras', 'Petrobras'), ('Consorcio', 'Parceria'))
    ANO_INICIO = 2020
    ANO_CHOICES = [(ano, ano) for ano in range(ANO_INICIO, date.today().year + 1)]
    TIPO_CHOICES = (('Inservivel','Inservivel'), ('Sucata', 'Sucata'))
 
    status =forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),choices=STATUS_CHOICES, required=False)
    ano = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),choices=ANO_CHOICES, required=False)
    
    al = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'data-role':'tagsinput'}),label="AL:", required=False)
    armazenamento = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),choices=ARMAZEM_CHOICES, required=False)
    tipo_venda = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),choices=VENDA_CHOICES, required=False)
    tipo_material = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),choices=TIPO_CHOICES, required=False)
    nm = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'data-role':'tagsinput'}),label="NM:", required=False)
    isa_sipa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm', 'data-role':'tagsinput'}),label="SIPA:", required=False)
    prioridade =forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}),choices=PRIORIDADE_CHOICES, required=False)

    
   # isasipa = forms.ModelMultipleChoiceField(queryset=LOTE.objects.filter('lote_isaSipa').order_by('gere_nome'), required=False, widget=forms.SelectMultiple(attrs={'class':'form-control form-control-sm'}))
   