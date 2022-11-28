import jdatetime
from django import template

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='date_string_to_jalali')
def date_string_to_jalali(datestring):
    persiandate = jdatetime.datetime.fromgregorian(day=datestring.day, month=datestring.month, year=datestring.year,
                                                   hour=datestring.hour, minute=datestring.minute, second=datestring.second)
    return persiandate.strftime("%Y/%m/%d %H:%M:%S")


@register.filter(name='show_activation')
def show_activation(activation):
    if activation:
        return "فعال"
    else:
        return "غیر فعال"


