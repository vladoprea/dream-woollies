from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):

    return price * quantity

@register.filter(name='calc_subtotal_discount')
def calc_subtotal_discount(discount_price, quantity):

    return discount_price * quantity