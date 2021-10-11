from django import template

register = template.Library()

@register.simple_tag
def update_estado(datos):
    print(datos)
    # id_uh = datos.get('id')
    # estado = datos.get('estado')
    # print(id_uh)
    # print(estado)


