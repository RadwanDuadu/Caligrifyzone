from django.test import TestCase
from decimal import Decimal

from checkout.models import Order, OrderLineItem
from products.models import Product


class TestOrderLineItemSignals(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            price=Decimal('10.00'),
            inventory=10,
        )

        self.order = Order.objects.create(
            full_name='Test User',
            email='test@test.com',
            phone_number='123456789',
            country='IE',
            postcode='D01',
            town_or_city='Dublin',
            street_address1='123 Street',
        )

    def test_order_total_updates_on_lineitem_create(self):
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )

        self.order.refresh_from_db()
        self.assertEqual(self.order.order_total, Decimal('20.00'))

    def test_order_total_updates_on_lineitem_delete(self):
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3,
        )

        self.order.refresh_from_db()
        self.assertEqual(self.order.order_total, Decimal('30.00'))

        line_item.delete()

        self.order.refresh_from_db()
        self.assertEqual(self.order.order_total, Decimal('0.00'))
