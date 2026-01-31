from decimal import Decimal

from django.test import TestCase
from django.conf import settings

from checkout.models import Order, OrderLineItem
from products.models import Product


class TestOrderAndOrderLineItemModels(TestCase):

    def setUp(self):
        """Create a product and order for testing"""
        self.product = Product.objects.create(
            name="Test Product",
            sku="TESTSKU123",
            price=Decimal("50.00"),
            inventory=10,
        )

        self.order = Order.objects.create(
            full_name="Test User",
            email="test@test.com",
            phone_number="123456789",
            country="GB",
            town_or_city="London",
            street_address1="123 Test Street",
            original_bag="{}",
            stripe_pid="test_pid_123",
        )

    def test_order_number_is_generated_on_save(self):
        """Order number is automatically generated"""
        self.assertTrue(self.order.order_number)
        self.assertEqual(len(self.order.order_number), 32)

    def test_lineitem_total_is_calculated_on_save(self):
        """Line item total equals product price * quantity"""
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )

        self.assertEqual(
            line_item.lineitem_total,
            self.product.price * 2
        )

    def test_order_total_updates_when_lineitem_created(self):
        """Order total updates via signal when line item is added"""
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

        self.order.refresh_from_db()
        self.assertEqual(self.order.order_total, Decimal("50.00"))

    def test_delivery_cost_applied_below_free_threshold(self):
        """Delivery cost added when below free delivery threshold"""
        OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )

        self.order.refresh_from_db()

        expected_delivery = (
            self.order.order_total
            * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
            / 100
        )

        self.assertEqual(self.order.delivery_cost, expected_delivery)
        self.assertEqual(
            self.order.grand_total,
            self.order.order_total + expected_delivery
        )

    def test_free_delivery_applied_above_threshold(self):
        """Delivery cost is zero when free delivery threshold met"""
        expensive_product = Product.objects.create(
            name="Expensive Product",
            sku="EXPENSIVE123",
            price=settings.FREE_DELIVERY_THRESHOLD,
            inventory=5,
        )

        OrderLineItem.objects.create(
            order=self.order,
            product=expensive_product,
            quantity=1,
        )

        self.order.refresh_from_db()

        self.assertEqual(self.order.delivery_cost, 0)
        self.assertEqual(
            self.order.grand_total,
            self.order.order_total
        )

    def test_order_total_updates_when_lineitem_deleted(self):
        """Order total updates when a line item is removed"""
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
        )

        line_item.delete()
        self.order.refresh_from_db()

        self.assertEqual(self.order.order_total, 0)
        self.assertEqual(self.order.grand_total, 0)
