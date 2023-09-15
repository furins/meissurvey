from modeltranslation.translator import translator, TranslationOptions
from .models import Quesito, Questionario

class QuesitoTranslationOptions(TranslationOptions):
    fields = ('titolo', 'introduzione', 'conclusione')

class QuestionarioTranslationOptions(TranslationOptions):
   fields = ('titolo', 'introduzione', 'conclusione')

translator.register(Quesito, QuesitoTranslationOptions)
translator.register(Questionario, QuestionarioTranslationOptions)
