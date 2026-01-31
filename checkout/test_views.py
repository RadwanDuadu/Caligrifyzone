from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch

from products.models import Product
from checkout.models import Order


class TestCheckoutViews(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=10,
            inventory=20,
        )

        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

        self.bag = {
            str(self.product.id): 2
        }

        self.checkout_url = reverse('checkout')

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_page_loads(self, mock_stripe):
        mock_stripe.return_value.client_secret = 'test_secret'

        session = self.client.session
        session['bag'] = self.bag
        session.save()

        response = self.client.get(self.checkout_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertIn('order_form', response.context)

    def test_checkout_redirects_if_bag_empty(self):
        response = self.client.get(self.checkout_url)
        self.assertRedirects(response, reverse('products'))

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_post_creates_order(self, mock_stripe):
        mock_stripe.return_value.client_secret = 'test_secret'

        session = self.client.session
        session['bag'] = self.bag
        session.save()

        response = self.client.post(self.checkout_url, {
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '123456789',
            'country': 'IE',
            'postcode': 'D01',
            'town_or_city': 'Dublin',
            'street_address1': '123 Street',
            'street_address2': '',
            'county': 'Dublin',
            'client_secret': 'pi_test_secret',
        })

        order = Order.objects.first()

        self.assertRedirects(
            response,
            reverse('checkout_success', args=[order.order_number])
        )

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_inventory_reduced_after_checkout(self, mock_stripe):
        mock_stripe.return_value.client_secret = 'test_secret'

        session = self.client.session
        session['bag'] = self.bag
        session.save()

        self.client.post(self.checkout_url, {
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '123456789',
            'country': 'IE',
            'postcode': 'D01',
            'town_or_city': 'Dublin',
            'street_address1': '123 Street',
            'street_address2': '',
            'county': 'Dublin',
            'client_secret': 'pi_test_secret',
        })

        self.product.refresh_from_db()
        self.assertEqual(self.product.inventory, 18)

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data(self, mock_modify):
        session = self.client.session
        session['bag'] = self.bag
        session.save()

        response = self.client.post(
            reverse('cache_checkout_data'),
            {
                'client_secret': 'pi_test_secret',
                'save_info': 'true',
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_checkout_success_page(self):
        order = Order.objects.create(
            full_name='Test User',
            email='test@test.com',
            phone_number='123456789',
            country='IE',
            postcode='D01',
            town_or_city='Dublin',
            street_address1='123 Street',
            county='Dublin',
            original_bag='{}',
            stripe_pid='test_pid',
        )

        response = self.client.get(
            reverse('checkout_success', args=[order.order_number])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'checkout/checkout_success.html'
        )