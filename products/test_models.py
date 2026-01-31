from django.test import TestCase
from products.models import Product, Category
from django.core.exceptions import ValidationError


class TestCategoryModel(TestCase):

    def test_str_method_returns_name(self):
        category = Category.objects.create(name="Calligraphy")
        self.assertEqual(str(category), "Calligraphy")

    def test_get_friendly_name_returns_friendly_or_name(self):
        category_with_friendly = Category.objects.create(
            name="Brush Pens", friendly_name="Beautiful Brush Pens"
        )
        category_without_friendly = Category.objects.create(name="Markers")

        self.assertEqual(category_with_friendly.get_friendly_name(),
                         "Beautiful Brush Pens")
        self.assertEqual(category_without_friendly.get_friendly_name(),
                         "Markers")


class TestProductModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Calligraphy")

    def test_str_method_returns_name(self):
        product = Product.objects.create(
            category=self.category,
            name="Fountain Pen",
            description="A smooth fountain pen.",
            price=15.00,
            inventory=10,
        )
        self.assertEqual(str(product), "Fountain Pen")

    def test_inventory_min_value_validator(self):
        product = Product(
            category=self.category,
            name="Invalid Pen",
            description="Negative inventory",
            price=5.00,
            inventory=-1
        )
        with self.assertRaises(ValidationError):
            product.full_clean()  # triggers validators

    def test_inventory_max_value_validator(self):
        product = Product(
            category=self.category,
            name="Too Many Pens",
            description="Exceeds max inventory",
            price=5.00,
            inventory=100
        )
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_rating_field_allows_blank_and_null(self):
        product = Product.objects.create(
            category=self.category,
            name="Pen with no rating",
            description="Rating can be blank",
            price=10.00,
            inventory=5,
            rating=None
        )
        self.assertIsNone(product.rating)
