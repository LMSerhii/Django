from django import template
from carusel.models import CmsSlider

register = template.Library()


@register.inclusion_tag('pizza/list_categories.html')
def get_slider():
    slide_list = CmsSlider.objects.all()
    return {'slide_list': slide_list}
