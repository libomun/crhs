from django import template
from django.utils.safestring import mark_safe
from re import IGNORECASE, compile, escape as rescape

register = template.Library()


@register.filter(name='highlight')
def highlight(text, search):
    rgx = compile(rescape(search), IGNORECASE)
    return mark_safe(
        rgx.sub(
            lambda m: '<b  style="font-weight:bold;color:#FC555">{}</b>'.format(m.group()),
            text
        )
    )

