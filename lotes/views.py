from django.shortcuts import render
from lotes.models import Lote 
from lotes.forms import  FormConsultarLote
from django.db.models import Count, Q, Sum, F,CharField, Value as V, FloatField
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test
# Create your views here.


@login_required  
def BuscarLotes(request):

    if request.method=="POST":
        start_time=time.time()   
        usuario=request.user.get_full_name()
        
        form_consultar_lote = FormConsultarLote(request.POST)
        if form_consultar_lote.is_valid(): 
            
            lista_final = []
            status= form_busca_lote.cleaned_data["status"] #padrão para variáveis snake case
            lote = form_busca_lote.cleaned_data["lote"]
            ano = form_busca_lote.cleaned_data["ano"] 
            gerencia = form_busca_lote.cleaned_data["gerencia"]
            proprietario = form_busca_lote.cleaned_data["proprietario"]
            al = form_busca_lote.cleaned_data["al"]
            responsavel = form_busca_lote.cleaned_data["responsavel"]
            armazenamento = form_busca_lote.cleaned_data["armazenamento"]
            tipo_venda = form_busca_lote.cleaned_data["tipo_venda"]
            tipo_material = form_busca_lote.cleaned_data["tipo_lote"]
            nm = form_busca_lote.cleaned_data["nm"]
            isa_sipa= form_busca_lote.cleaned_data["isasipa"]
            leilao= form_busca_lote.cleaned_data["leilao"]
            prioridade = form_busca_lote.cleaned_data["prioridade"]
            check =form_busca_lote.cleaned_data["check"]
         
            lista = Lote.objects.all()
           
            if lote:  
                lote = lote.split(',')   
                query = Q(Codigo=0)  
                for a in lote:   
                    query.add(Q(Codigo__icontains=a), Q.OR)    
                lista = lista.filter(query) 
           
            if ano:  
                queryA = Q(Ano=0) 
                  
                for anos in ano:
                    queryA.add(Q(Ano=anos), Q.OR)  
                lista = lista.filter(queryA)
            
           
            if proprietario: 
                queryC = Q(Proprietario="a") 
                for prop in proprietario:
                    queryC.add(Q(Proprietario=prop), Q.OR)
                lista = lista.filter(queryC)
            
            if al:    
                al = al.split(',')
                queryD = Q(Al="a")
                for b in al:
                    queryD.add(Q(Al__iexact=b), Q.OR)
                lista = lista.filter(queryD)
            
            if responsavel:  
                queryE = Q(Responsavel=0)
                for resp in responsavel:
                    queryE.add(Q(Responsavel=resp.id), Q.OR)
                lista = lista.filter(queryE)
            
         
            
            if armazenamento:
                queryG = Q(Armazenamento="a")
                for armazem in localArmazenamento:
                    queryG.add(Q(Armazenamento=armazem), Q.OR)
                lista = lista.filter(queryG)
            
            if tipo_venda:
                queryH = Q(TipoVenda="a")
                for tipo in tipoVenda:
                    queryH.add(Q(TipoVenda=tipo), Q.OR)
                lista = lista.filter(queryH)
            
            if tipo_material:
                queryK = Q(TipoMaterial="a")
                for tipLote in tipoLote:
                    queryK.add(Q(lote_tipoLote=tipLote), Q.OR)
                lista = lista.filter(queryK)

            if isa_sipa:  
                isa_sipa = isa_sipa.split(',')  
                queryI = Q(IsaSipa="a")    
                for sip in isasipa:
                    queryI.add(Q(IsaSipa=sip), Q.OR)    
                lista = lista.filter(queryI) 
            
         

            if status:  
                queryY = Q(Status="a")
                for sta in status:
                    queryY.add(Q(Status=sta), Q.OR)
                lista = lista.filter(queryY) 
  
                  
               
                  
                lista = lista.filter(queryL)  
                    
            if prioridade:  
                queryM = Q(Prioridade="a")
                for csta in prioridade:
                    queryM.add(Q(Prioridade=csta), Q.OR)
                lista = lista.filter(queryM)

                
            return render(request, 'consultar_lotes.html', {
             
                'lotes':lista,
                'form_consultar_lote': form_consultar_lote,
                
            })
        else:
            lista = None
            return render(request, 'consultar_lotes.html', {
                'lotes':lista,
                'form_consultar_lote': form_consultar_lote
            })
    else: 
        lista = None   
        return render(request, 'lotes/consultar_lotes.html', {   
            'lotes':lista,
            'form_consultar_lote':FormConsultarLote()    
        })