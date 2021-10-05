from django import template

register = template.Library()

@register.simple_tag
def get_id(path):
    id = path.split('/')[-1]
    return id


@register.simple_tag
def separate_name(name):
    first_name = name.split('-')[0]
    return first_name
