from __future__ import unicode_literals

from django.template import Library
from django.template.loader import get_template
register = Library()


@register.simple_tag
def admin_modal_filter(cl, spec):
    tpl = get_template("gentelella/modal_filter.html")
    return tpl.render({
        'title': spec.title,
        'choices': list(spec.choices(cl)),
        'spec': spec,
    })