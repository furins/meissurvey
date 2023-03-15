from django.contrib import admin
from .models import Questionario, Quesito, Risposta
from ordered_model.admin import OrderedModelAdmin

@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'slug', 'inizio', 'fine')
    prepopulated_fields = {"slug": ("titolo",)}

@admin.register(Quesito)
class QuesitoAdmin(OrderedModelAdmin):
    list_display = ('get_slug_questionario', 'titolo', 'tipo', 'opzioni', 'move_up_down_links')
    list_filter = ('questionario__slug',)
    
    @admin.display(description='Questionario')
    def get_slug_questionario(self, obj):
        return obj.questionario.slug

@admin.register(Risposta)
class RispostaAdmin(admin.ModelAdmin):
    list_display = ('get_slug_questionario', 'get_titolo_quesito', 'risposta', 'data_risposta')
    list_filter = ('questionario__slug',)
        
    @admin.display(description='Questionario')
    def get_slug_questionario(self, obj):
        return obj.questionario.slug
    
    @admin.display(description='Quesito')
    def get_titolo_quesito(self, obj):
        return obj.quesito.titolo