from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, item_data):
    """
    Calculate subtotal for items with or without sizes
    """
    if isinstance(item_data, dict):
        quantity = sum(item_data['items_by_size'].values())
    else:
        quantity = item_data

    return price * quantity