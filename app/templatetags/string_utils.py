from django import template

register = template.Library()


@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, str):
        return text.startswith(starts)
    return False


@register.filter('titlefy')
def titlefy(text):
    return " ".join(text.split('-')[::-1]).title()


@register.filter('to_list')
def to_list(value):
    return list(value)
