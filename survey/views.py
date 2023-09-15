import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.timezone import now
from survey.models import Quesito, Questionario, Risposta

def intro(request):
    return render(request, 'survey/intro.html', context={})

def conclusione(request):
    return render(request, 'survey/fine.html', context={})

def iscrizione(request):
    return render(request, 'survey/newsletter.html', context={})

def ringraziamento_iscrizione(request):
    return render(request, 'survey/success.html', context={})

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
                return redirect(reverse('conclusione'))

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
