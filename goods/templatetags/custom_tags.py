from django import template

register = template.Library()

@register.simple_tag
def change_params(params):
    return modified_params
