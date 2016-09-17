from django.template.defaultfilters import slugify
from django import template

register = template.Library()


@register.filter
def slug(value):
    return slugify(value)


@register.filter
def short_time_format(value):
    return "{}".format(value)
