from ..models import HotPic
from django import template
register = template.Library()

@register.simple_tag
def gethot_pics():
    return HotPic.objects.all()
