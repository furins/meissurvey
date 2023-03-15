import json
from django.shortcuts import render
from django.utils.timezone import now
from survey.models import Quesito, Questionario, Risposta

def questionario(request, slug_questionario):
    try:
        q = Questionario.objects.get(slug=slug_questionario)
        if q not in Questionario.objects.attivi():
            return render(
                request, 
                'survey/questionario_non_attivo.html', 
                context={'slug_questionario':slug_questionario}
                )
        quesito = q.quesito_set.first() # questo è il questionario in caso di un GET
        
        if request.method == 'POST':
            # salvo di dati
            quesito=Quesito.objects.get(id=int(request.POST.get('quesito')))
            risposta = Risposta(
                questionario=q, 
                quesito=quesito, 
                risposta={"value":request.POST.get('risposta')},
                data_risposta=now()
                )
            risposta.save()
            
            quesito = quesito.next() # passo al successivo
            
            if quesito is None:
                quesito = q.quesito_set.first() # Si ricomincia
                
        return render(
            request, 
            'survey/questionario.html', 
            context={'questionario':q, "quesito":quesito}
            )
    except Questionario.DoesNotExist:
        return render(
            request, 
            'survey/questionario_non_esistente.html', 
            context={'slug_questionario':slug_questionario}
            )
