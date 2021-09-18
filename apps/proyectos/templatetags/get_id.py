from django import template

register = template.Library()

@register.simple_tag
def get_id(path):
    id = path.split('/')[-1]
    return id
