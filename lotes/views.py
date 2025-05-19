from django.shortcuts import render
from lotes.models import Lote 
from lotes.forms import  FormConsultarLote
from django.db.models import Count, Q, Sum, F,CharField, Value as V, FloatField
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required  
def BuscarLotes(request):

    if request.method=="POST": 
       
      
         #padrão para variáveis snake case
        form_consultar_lote = FormConsultarLote(request.POST)
        if form_consultar_lote.is_valid(): 
            
           
            status= form_consultar_lote.cleaned_data["status"] 
            lote = form_consultar_lote.cleaned_data["lote"]
            ano = form_consultar_lote.cleaned_data["ano"] 
        
          
            al = form_consultar_lote.cleaned_data["al"]
            armazenamento = form_consultar_lote.cleaned_data["armazenamento"]
            tipo_venda = form_consultar_lote.cleaned_data["tipo_venda"]
            tipo_material = form_consultar_lote.cleaned_data["tipo_material"]
            isa_sipa= form_consultar_lote.cleaned_data["isa_sipa"]
            prioridade = form_consultar_lote.cleaned_data["prioridade"]
        
         
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
            
           
        
            if al:    
                al = al.split(',')
                queryD = Q(Al="a")
                for b in al:
                    queryD.add(Q(Al__iexact=b), Q.OR)
                lista = lista.filter(queryD)
            
          
         
            
            if armazenamento:
                queryG = Q(LocalArmazenamento="a")
                for armazem in armazenamento:
                    queryG.add(Q(LocalArmazenamento=armazem), Q.OR)
                lista = lista.filter(queryG)
            
            if tipo_venda:
                queryH = Q(TipoVenda="a")
                for tipo in tipo_venda:
                    queryH.add(Q(TipoVenda=tipo), Q.OR)
                lista = lista.filter(queryH)
            
            if tipo_material:
                queryK = Q(TipoMaterial="a")
                for tipLote in tipo_material:
                    queryK.add(Q(lote_tipoLote=tipLote), Q.OR)
                lista = lista.filter(queryK)

            if isa_sipa:  
                isa_sipa = isa_sipa.split(',')  
                queryI = Q(IsaSipa="a")    
                for sip in isa_sipa:
                    queryI.add(Q(IsaSipa=sip), Q.OR)    
                lista = lista.filter(queryI) 
            
         

            if status:  
                queryY = Q(Status="a")
                for sta in status:
                    queryY.add(Q(Status=sta), Q.OR)
                lista = lista.filter(queryY) 
  
        
                    
            if prioridade:  
                queryM = Q(Prioridade="a")
                for csta in prioridade:
                    queryM.add(Q(Prioridade=csta), Q.OR)
                lista = lista.filter(queryM)

                
            return render(request, 'lotes/consultar_lotes.html', {
             
                'lotes':lista,
                'form_consultar_lote': form_consultar_lote,
                
            })
        else:
            lista = None
            return render(request, 'lotes/consultar_lotes.html', {
                'lotes':lista,
                'form_consultar_lote': form_consultar_lote
            })
    else: 
        lista = None   
        return render(request, 'lotes/consultar_lotes.html', {   
            'lotes':lista,
            'form_consultar_lote':FormConsultarLote()    
        })