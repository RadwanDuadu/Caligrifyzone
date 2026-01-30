from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

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
    """ Add product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    # ---------- PRODUCTS WITH SIZES ----------
    if size:
        # If item exists but was previously stored as int, convert it
        if item_id in bag and isinstance(bag[item_id], int):
            bag[item_id] = {'items_by_size': {}}

        if item_id not in bag:
            bag[item_id] = {'items_by_size': {}}

        if size in bag[item_id]['items_by_size']:
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity'
            )
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag'
            )
    # ---------- PRODUCTS WITHOUT SIZES ----------
    else:
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity'
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Added {product.name} to your bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)



def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)

    item_id = str(item_id)

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
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    item_id = str(item_id)  

    try:
        bag = request.session.get('bag', {})
        size = request.POST.get('product_size')

        # Convert string 'None' to actual None
        if size == 'None':
            size = None

        if size:
            del bag[item_id]['items_by_size'][size]

            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)

            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f'Removed {product.name} from your bag'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except KeyError:
        messages.error(request, 'Item not found in bag')
        return HttpResponse(status=404)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)