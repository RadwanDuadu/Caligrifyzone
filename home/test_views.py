# home/tests.py
from django.test import TestCase
from django.urls import reverse


class TestHomeViews(TestCase):

    def test_index_view_status_code(self):
        """Test that the index page loads successfully"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self):
        """Test that the correct template is used for index page"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'home/index.html')
