from pyexpat import model
from django.db import models
from django.utils import timezone
from ordered_model.models import OrderedModel
from ckeditor.fields import RichTextField

class Risposta(models.Model):
    questionario = models.ForeignKey('Questionario', on_delete=models.CASCADE)
    quesito = models.ForeignKey('Quesito', on_delete=models.CASCADE)
    risposta = models.JSONField(null=True, blank=True)
    data_risposta = models.DateTimeField(auto_created=True)

    def __str__(self):
        try:
            if self.risposta is not None:
                return f'risposta del {self.data_risposta} alla domanda {self.quesito}: {self.risposta["value"]}'
        except AttributeError:
            return f'risposta del {self.data_risposta} alla domanda {self.quesito}: -'
        return f'risposta del {self.data_risposta} alla domanda {self.quesito}: -'
    class Meta:
        verbose_name_plural = "risposte"
    
        
class Quesito(OrderedModel):
    class TipiQuesito(models.IntegerChoices):
        DOMANDA = 1, 'Domanda aperta'
        GRADIMENTO_5 = 2, 'Gradimento, scala da 1 a 5'
        GRADIMENTO_6 = 3, 'Gradimento, scala da 1 a 6'
        
    questionario = models.ForeignKey('Questionario', on_delete=models.CASCADE)
    titolo = models.CharField(max_length=250)
    introduzione = RichTextField(default='', blank=True)
    conclusione = RichTextField(default='', blank=True)
    tipo = models.IntegerField(choices=TipiQuesito.choices, default=TipiQuesito.GRADIMENTO_5)
    opzioni = models.JSONField(null=True, blank=True)
    
    order_with_respect_to = 'questionario'

    def __str__(self):
        return f'{self.titolo}'

    class Meta(OrderedModel.Meta):
        verbose_name_plural = "quesiti"   


class QuestionarioManager(models.Manager):
    def attivi(self):
        t = timezone.localtime(timezone.now())
        return super().get_queryset().filter(inizio__lte=t,fine__gte=t)

class Questionario(models.Model):
    objects = QuestionarioManager()
    
    titolo = models.CharField(max_length=250)
    introduzione = RichTextField(default='', blank=True)
    conclusione = RichTextField(default='', blank=True)
    slug = models.SlugField(max_length=50)
    inizio = models.DateTimeField()
    fine = models.DateTimeField()
    
    def __str__(self):
        return f'{self.slug}'

    class Meta:
        verbose_name_plural = "questionari"