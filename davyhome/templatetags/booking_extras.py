from django.template.defaultfilters import slugify
from django import template

register = template.Library()


@register.filter
def slug(value):
    return slugify(value)


@register.filter
def short_time_format(value):
    return "{}".format(value)


@register.filter
def status_format(value):
    status = {
        'CF': 'Confirmed',
        'CM': 'Completed',
        'UF': 'Unfulfilled',
        'CN': 'Canceled'
    }

    return status.get(value, value)
