from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from checkout.models import Order
from .models import UserProfile


class TestProfilesViews(TestCase):
    def setUp(self):
        """Set up a user and profile for testing"""
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', email='test@example.com',
            password='testpass123'
        )
        self.profile, created = UserProfile.objects.get_or_create(
            user=self.user,
            defaults={
                'default_phone_number': '1234567890',
                'default_country': 'US',
                'default_postcode': '12345',
                'default_town_or_city': 'Test City',
                'default_street_address1': '123 Test Street',
            }
        )
        # Log in the user for views requiring authentication
        self.client.login(username='testuser', password='testpass123')

    def test_profile_view_status_code_and_template(self):
        """Profile view loads correctly for logged-in user"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_view_redirects_if_not_logged_in(self):
        """Profile view should redirect if user not logged in"""
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_post_updates_profile(self):
        """POST request updates profile and shows success message"""
        response = self.client.post(
            reverse('profile'),
            {
                'default_phone_number': '9876543210',
                'default_country': 'US',
                'default_postcode': '54321',
                'default_town_or_city': 'New City',
                'default_street_address1': '456 New Street',
            },
            follow=True
        )
        self.assertContains(response, 'Profile updated successfully')
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, '9876543210')

    def test_order_history_view_status_and_template(self):
        """Order history page loads correctly"""
        order = Order.objects.create(
            order_number='123ABC',
            user_profile=self.profile,
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='US',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test Street',
            grand_total=50.00,
        )
        response = self.client.get(reverse('order_history', args=['123ABC']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(
            response,
            'This is a past confirmation for order number 123ABC')

    def test_order_history_nonexistent_order_returns_404(self):
        """Accessing a non-existent order returns 404"""
        response = self.client.get(reverse('order_history',
                                           args=['INVALID123']))
        self.assertEqual(response.status_code, 404)
