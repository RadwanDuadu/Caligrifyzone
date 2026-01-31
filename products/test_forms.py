from django.test import TestCase
from products.forms import ProductForm
from products.models import Category


class TestProductForm(TestCase):
    """Tests for the ProductForm"""

    def setUp(self):
        # Create a category so the form has valid choices
        self.category = Category.objects.create(name="Test Category",
                                                friendly_name="Test Category")

    def test_product_form_valid_data(self):
        """Test that form is valid with correct data"""
        form_data = {
            'category': self.category.id,
            'name': 'Test Product',
            'description': 'A test product',
            'price': 25.00,
            'inventory': 5,
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_product_form_missing_required_fields(self):
        """Test that form is invalid if required fields are missing"""
        form_data = {
            'category': '',  # intentionally blank
            'name': '',
            'description': '',
            'price': '',
            'inventory': '',
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('price', form.errors)
        self.assertIn('inventory', form.errors)
