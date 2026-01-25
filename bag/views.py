from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    bag = request.session.get('bag', {})
    bag_items = []

    for item_id, item_data in bag.items():
        product = Product.objects.get(pk=item_id)

        # Product WITHOUT sizes
        if isinstance(item_data, int):
            bag_items.append({
                'item_id': item_id,
                'product': product,
                'quantity': item_data,
                'size': None,
            })

        # Product WITH sizes
        else:
            for size, quantity in item_data['items_by_size'].items():
                bag_items.append({
                    'item_id': item_id,
                    'product': product,
                    'quantity': quantity,
                    'size': size,
                })

    total = sum(item['product'].price * item['quantity'] for item in bag_items)
    delivery = 0
    grand_total = total
    free_delivery_delta = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
        'free_delivery_delta': free_delivery_delta,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    quantity_str = request.POST.get('quantity')
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    try:
        quantity = int(quantity_str)
    except (TypeError, ValueError):
        return redirect(reverse('view_bag'))

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)
    
    except Exception as e:
        return HttpResponse(status=500)