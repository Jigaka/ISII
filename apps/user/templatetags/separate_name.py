from django import template

register = template.Library()

@register.simple_tag
def separate_name(name):
    nombre = name.__str__()
    first_name = nombre.split('-')[0]
    return first_name
