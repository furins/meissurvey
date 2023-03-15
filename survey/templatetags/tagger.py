from django import template

register = template.Library()

@register.simple_tag
def getManager(obj):
    return obj._meta.model.objects