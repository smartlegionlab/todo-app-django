import datetime
import re

import pytz
from django import template

register = template.Library()


@register.filter
def custom_date(value, timezone='Asia/Novosibirsk'):
    if isinstance(value, str):
        try:
            date_value = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return value
    else:
        date_value = value
    if date_value.tzinfo is None:
        date_value = pytz.utc.localize(date_value)
    target_timezone = pytz.timezone(timezone)
    date_value = date_value.astimezone(target_timezone)
    return date_value.strftime('%d.%m.%Y %H:%M:%S')


@register.filter
def obfuscate_token(token):
    if len(token) <= 8:
        return token
    return f"{token[:4]}{'*' * 4}{token[-4:]}"


@register.filter
def urlize_with_target(value):
    urlize = template.defaultfilters.urlize(value)
    return re.sub(r'<a href="(.*?)"', r'<a href="\1" target="_blank"', urlize)


@register.filter
def mask_email(email):
    if '@' in email:
        local_part, domain = email.split('@')
        return f"{local_part[:2]}**@**{domain[-2:]}"
    return email
