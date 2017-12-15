from django import template

register = template.Library()


@register.filter
def get_value(d, key):
    return d.get(key)
