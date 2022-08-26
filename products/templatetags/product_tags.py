from django import template

register = template.Library()

@register.filter
def div_nutrition(value):
    """Divides value by 3 to 2 decimal points"""
    return round((value/3), 2)
