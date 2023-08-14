from django import template
from jalali_date import date2jalali

register = template.Library()

@register.filter(name="cut")
def cut(value, args):
    return value.replace(args, "****")

@register.filter(name="jalali")
def show_jalali_date(value):
    return date2jalali(value)