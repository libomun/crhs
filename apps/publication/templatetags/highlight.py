from django import template
from django.utils.safestring import mark_safe
import re
register = template.Library()


@register.filter
def highlight_search(text, search):
    highlighted = re.sub('(?i)(%s)' % (re.escape(search)),
                         '<span style="font-weight:bold;color:#FC5531" class="highlight"">\\1</span>', text)
    return mark_safe(highlighted)


