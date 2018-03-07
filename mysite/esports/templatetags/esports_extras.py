from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def lstrip(value):
    return value.lstrip("[]1234567890',.\" ")

@register.filter
def lower(value):
    return value.lower()

@register.filter
def get_dict_item(value, team):
    return value[team]
