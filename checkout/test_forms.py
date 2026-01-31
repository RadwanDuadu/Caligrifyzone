from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):

    def test_order_form_is_valid(self):
        """Test OrderForm with all required fields"""
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '123456789',
            'street_address1': '123 Street',
            'town_or_city': 'Dublin',
            'postcode': 'D01',
            'country': 'IE',
            'county': 'Dublin',
        })
        self.assertTrue(form.is_valid())

    def test_full_name_is_required(self):
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '123456789',
            'street_address1': '123 Street',
            'town_or_city': 'Dublin',
            'postcode': 'D01',
            'country': 'IE',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)

    def test_email_is_required(self):
        form = OrderForm({
            'full_name': 'Test User',
            'email': '',
            'phone_number': '123456789',
            'street_address1': '123 Street',
            'town_or_city': 'Dublin',
            'postcode': 'D01',
            'country': 'IE',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_street_address1_is_required(self):
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '123456789',
            'street_address1': '',
            'town_or_city': 'Dublin',
            'postcode': 'D01',
            'country': 'IE',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors)

    def test_full_name_has_autofocus(self):
        form = OrderForm()
        self.assertIn(
            'autofocus',
            form.fields['full_name'].widget.attrs
        )

    def test_placeholders_include_asterisk_for_required_fields(self):
        form = OrderForm()
        self.assertEqual(
            form.fields['full_name'].widget.attrs['placeholder'],
            'Full Name *'
        )

    def test_country_field_has_form_control_class_only(self):
        form = OrderForm()
        self.assertEqual(
            form.fields['country'].widget.attrs['class'],
            'form-control'
        )

    def test_non_country_fields_have_stripe_class(self):
        form = OrderForm()
        self.assertIn(
            'stripe-style-input',
            form.fields['email'].widget.attrs['class']
        )

    def test_all_labels_are_false(self):
        form = OrderForm()
        for field in form.fields.values():
            self.assertFalse(field.label)
