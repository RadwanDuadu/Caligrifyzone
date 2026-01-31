from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):
    """Tests for the home app views"""

    def test_home_view_status_code(self):
        """Test that the home page loads successfully"""
        response = self.client.get(reverse('home'))  # use 'home', not 'index'
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        """Test that the correct template is used for home page"""
        response = self.client.get(reverse('home'))  # use 'home'
        self.assertTemplateUsed(response, 'home/index.html')
